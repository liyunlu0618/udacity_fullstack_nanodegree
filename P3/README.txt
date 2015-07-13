1. To start the application, run the following commands sequentially:

python database_setup.py
python add_items.py
python webserver.py

Visit the website using the url: http://localhost:8000

2. Basic functionalities
1) Login/Logout
	There's login/logout link on every page of the app. Only google plus account is supported now.
2) Public pages -- without logging in
	User is only able to view all categories and items without loggin in.
3) User specific pages -- after logging in
	Authenticated and authorized users could add categories, add/update/delete items belong to him/her.
	Category deletion is not supported, since there might be items in the category which belong to other users.
4) Objects represented in JSON
	The following links could be used to get category, items and item data:
	'/catalog/JSON': all categories stored in the app
	'/catalog/<int:category_id>/item/JSON': all items with in a specific category
	'/catalog/<int:category_id>/item/<int:item_id>/JSON': info about a specific item