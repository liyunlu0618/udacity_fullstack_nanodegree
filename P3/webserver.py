from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"

# Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

@app.route('/logout')
def showLogout():
    gdisconnect()
    flash("Successfully logged out!")
    return redirect(url_for('showCategories'))

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code, now compatible with Python3
    request.get_data()
    code = request.data.decode('utf-8')

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    # Submit request, parse response - Python3 compatible
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    return output

def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

@app.route('/gdisconnect')
def gdisconnect():
        # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/catalog/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories = [c.serialize for c in categories])

@app.route('/catalog/<int:category_id>/item/JSON')
def itemsJSON(category_id):
    items = session.query(Item).filter_by(category_id = category_id).all()
    return jsonify(items = [i.serialize for i in items])

@app.route('/catalog/<int:category_id>/item/<int:item_id>/JSON')
def itemJSON(category_id, item_id):
    item = session.query(Item).filter_by(id = item_id).one()
    return jsonify(item.serialize)

# Show all categories and newly added items
@app.route('/')
@app.route('/catalog/')
def showCategories():
    categories = session.query(Category).order_by(asc(Category.name)).all()
    items = session.query(Item).order_by(desc(Item.time_added)).all()
    length = min(10, len(items))
    recentItems = []
    for i in range(0, 10):
        c = session.query(Category).filter_by(id = items[i].category_id).one()
        cname = c.name
        recentItems.append((items[i], cname))
    if 'username' not in login_session:
        loggedin = False
    else:
        loggedin = True
    if not loggedin:
        flash("After logging in, you can create/edit categories.")
    return render_template('index.html', categories = categories, recentItems = recentItems, loggedin = loggedin)

# Add new category
@app.route('/catalog/new', methods = ['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        loggedin = False
    else:
        loggedin = True
    if not loggedin:
        return redirect(url_for('showLogin'))
    if request.method == 'POST':
        if request.form['name']:
            newCategory = Category(name = request.form['name'])
            session.add(newCategory)
            session.commit()
            flash("New category %s successfully created!" % newCategory.name)
        return redirect(url_for('showCategories'))
    else:
        return render_template('new_category.html', loggedin = loggedin)

# Edit category
@app.route('/catalog/<int:category_id>/edit', methods = ['GET', 'POST'])
def editCategory(category_id):
    if 'username' not in login_session:
        loggedin = False
    else:
        loggedin = True
    if not loggedin:
        return redirect(url_for('showLogin'))
    category = session.query(Category).filter_by(id = category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            category.name = request.form['name']
        session.commit()
        flash("Category %s successfully edited!" % category.name)
        return redirect(url_for('showCategories'))
    else:
        return render_template('edit_category.html', category = category, loggedin = loggedin)


# We do not support the feature of category deletion, since there might 
# be items belong to other users in that category.


# Show all items in a category
@app.route('/catalog/<int:category_id>/item/')
def showItems(category_id):
    if 'username' not in login_session:
        loggedin = False
    else:
        loggedin = True
    if not loggedin:
        flash("After logging in, you can edit/delete movies you added.")
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category_id).all()
    return render_template('items.html', categories = categories, category = category, items = items, loggedin = loggedin)

# Show description of an item
@app.route('/catalog/<int:category_id>/item/<int:item_id>')
def showItem(category_id, item_id):
    if 'username' not in login_session:
        loggedin = False
    else:
        loggedin = True
    item = session.query(Item).filter_by(id = item_id).one()
    userAdded = True
    if 'username' not in login_session or item.user_id != login_session['user_id']:
        userAdded = False
    if not userAdded:
        flash("You're not logged in, or you're not the user created the movie, so you cannot edit/delete it.")
    return render_template('item.html', category_id = category_id, item = item, userAdded = userAdded, loggedin = loggedin)

# Add an item to a category
@app.route('/catalog/<int:category_id>/item/new', methods = ['GET', 'POST'])
def newItem(category_id):
    if 'username' not in login_session:
        loggedin = False
        return redirect(url_for('showLogin'))
    else:
        loggedin = True
    if request.method == 'POST':
        if request.form['name'] and request.form['description']:
            item = Item(name = request.form['name'], 
                description = request.form['description'], category_id = category_id,
                user_id = login_session['user_id'])
            session.add(item)
            session.commit()
        return redirect(url_for('showItems', category_id = category_id))
    else:
        category = session.query(Category).filter_by(id = category_id).one()
        return render_template('new_item.html', category = category, loggedin = loggedin)

# Edit an item under a category
@app.route('/catalog/<int:category_id>/item/<int:item_id>/edit', methods = ['GET', 'POST'])
def editItem(category_id, item_id):
    if 'username' not in login_session:
        loggedin = False
        return redirect(url_for('showLogin'))
    else:
        loggedin = True
    item = session.query(Item).filter_by(id = item_id).one()
    categories = session.query(Category).all()
    changeCategory = False
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        if request.form['category']:
            for c in categories:
                if c.name == request.form['category'] and c.id != category_id:
                    category_id = c.id
                    break
        item.category_id = category_id
        item.user_id = login_session['user_id']
        session.commit()
        flash("Successfully edited movie %s." % item.name)
        return redirect(url_for('showItems', category_id = category_id))
    else:
        return render_template('edit_item.html', categories = categories, item = item, loggedin = loggedin)

# Delete an item from a category
@app.route('/catalog/<int:category_id>/item/<int:item_id>/delete', methods = ['GET', 'POST'])
def deleteItem(category_id, item_id):
    item = session.query(Item).filter_by(id = item_id).one()
    if 'username' not in login_session:
        loggedin = False
        return redirect('/login')
    else:
        loggedin = True
    if item.user_id != login_session['user_id']:
        return "<script>function myFunction(){alert('You are not authorized to delete this movie.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(item)
        flash('%s Successfully Deleted' % item.name)
        session.commit()
        return redirect(url_for('showItems', category_id = category_id))
    else:
        return render_template('delete_item.html', item = item, loggedin = loggedin)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)