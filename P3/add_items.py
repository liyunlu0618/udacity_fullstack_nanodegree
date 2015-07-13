from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User
import time

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

Base.metadata.drop_all(bind=engine, checkfirst=True)
Base.metadata.create_all(engine)


# Create user 1
user1 = User(name="Yunlu Li", email="liyunlulu1990@gmail.com",
             picture='http://cishan.sznews.com/humor/attachement/jpg/site3/20100806/0050ba6b2e410dc5f7583a.jpg')
session.add(user1)
session.commit()

# Create user 2
user2 = User(name="Jingyu Wang", email="jingyuw1990@gmail.com",
             picture='http://att.bbs.duowan.com/forum/201401/23/2040124mz5veyv0p5gx50e.jpg')
session.add(user2)
session.commit()

# Animation
category1 = Category(name="Animation")

session.add(category1)
session.commit()


item1 = Item(user=user1, category=category1, name="Minions", description="Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world.")

session.add(item1)
session.commit()


item2 = Item(user=user1, category=category1, name="Inside Out", description="After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house, and school.")

session.add(item2)
session.commit()


item3 = Item(user=user2, category=category1, name="Home", description="Oh, an alien on the run from his own people, lands on Earth and makes friends with the adventurous Tip, who is on a quest of her own.")

session.add(item3)
session.commit()


item4 = Item(user=user1, category=category1, name="Big Hero 6", description="The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.")
session.add(item4)
session.commit()


# Comedy
category2 = Category(name="Comedy")

session.add(category2)
session.commit()


item1 = Item(user=user1, category=category2, name="Ted 2", description="Newlywed couple Ted and Tami-Lynn want to have a baby, but in order to qualify to be a parent, Ted will have to prove he's a person in a court of law.")

session.add(item1)
session.commit()


item2 = Item(user=user1, category=category2, name="Kingsman: The Secret Service", description="A spy organization recruits an unrefined, but promising street kid into the agency's ultra-competitive training program, just as a global threat emerges from a twisted tech genius.")

session.add(item2)
session.commit()


item3 = Item(user=user2, category=category2, name="Pixels", description="When aliens misinterpret video feeds of classic arcade games as a declaration of war, they attack the Earth in the form of the video games.")

session.add(item3)
session.commit()


item4 = Item(user=user2, category=category2, name="Pitch Perfect 2", description="After a humiliating command performance at Lincoln Center, the Barden Bellas enter an international competition that no American group has ever won in order to regain their status and right to perform.")
session.add(item4)
session.commit()


# Drama
category3 = Category(name="Drama")

session.add(category3)
session.commit()


item1 = Item(user=user1, category=category3, name="San Andreas", description="In the aftermath of a massive earthquake in California, a rescue-chopper pilot makes a dangerous journey across the state in order to rescue his daughter.")

session.add(item1)
session.commit()


item2 = Item(user=user1, category=category3, name="Gone Girl", description="With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent.")

session.add(item2)
session.commit()


item3 = Item(user=user1, category=category3, name="Fifty Shades of Grey", description="Literature student Anastasia Steele's life changes forever when she meets handsome, yet tormented, billionaire Christian Grey.")

session.add(item3)
session.commit()


item4 = Item(user=user2, category=category3, name="Cinderella", description="When her father unexpectedly passes away, young Ella finds herself at the mercy of her cruel stepmother and her daughters. Never one to give up hope, Ella's fortunes begin to change after meeting a dashing stranger.")
session.add(item4)
session.commit()


# Biography
category4 = Category(name="Biography")

session.add(category4)
session.commit()


item1 = Item(user=user1, category=category4, name="American Sniper", description="Navy SEAL sniper Chris Kyle's pinpoint accuracy saves countless lives on the battlefield and turns him into a legend. Back home to his wife and kids after four tours of duty, however, Chris finds that it is the war he can't leave behind.")

session.add(item1)
session.commit()


item2 = Item(user=user1, category=category4, name="The Imitation Game", description="During World War II, mathematician Alan Turing tries to crack the enigma code with help from fellow mathematicians.")

session.add(item2)
session.commit()


item3 = Item(user=user1, category=category4, name="The Theory of Everything", description="A look at the relationship between the famous physicist Stephen Hawking and his wife.")

session.add(item3)
session.commit()


item4 = Item(user=user1, category=category4, name="Schindler's List", description="In Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.")
session.add(item4)
session.commit()


# Science Fiction
category5 = Category(name="Science Fiction")

session.add(category5)
session.commit()


item1 = Item(user=user2, category=category5, name="Terminator Genisys", description="John Connor sends Kyle Reese back in time to protect Sarah Connor, but when he arrives in 1984, nothing is as he expected it to be.")

session.add(item1)
session.commit()


item2 = Item(user=user2, category=category5, name="Jurassic World", description="A new theme park is built on the original site of Jurassic Park. Everything is going well until the park's newest attraction--a genetically modified giant stealth killing machine--escapes containment and goes on a killing spree.")

session.add(item2)
session.commit()


item3 = Item(user=user1, category=category5, name="Guardians of the Galaxy", description="A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.")

session.add(item3)
session.commit()


item4 = Item(user=user2, category=category5, name="Interstellar", description="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.")
session.add(item4)
session.commit()

print "added movie items!"