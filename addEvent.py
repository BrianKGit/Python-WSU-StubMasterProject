# creates an event to add to EventTickets
import pymongo
import pprint

# cString = "mongodb+srv://om3705is:om3705ispassword@mongobkwsu-ljuj6.gcp.
# mongodb.net/test?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE"
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.EventTickets
Events = db.Events
Tickets = db.Tickets


class Event:

    # default constructor

    def __init__(self, name, category, location, time, lineup):
        # self.id = id
        self.name = name
        self.category = category
        self.location = location
        self.time = time
        self.lineup = lineup


class Category:
    def __init__(self, type, genre):
        self.type = type
        self.genre = genre


class Location:
    def __init__(self, city, state, venue):
        self.city = city
        self.state = state
        self.venue = venue


categ = Category('Music', 'Rock')
location = Location('Minneapolis', 'Mn', 'The Myth')

newEvent = Event('Van Down By The River', categ.__dict__, location.__dict__, 'time',
                 'lineup')


try:
    Events.insert_one(newEvent.__dict__)
    print('Event added')
except Exception as e:
    print("Insert failed", e)


docs = Events.find()
pretty = pprint.PrettyPrinter(indent=4)
try:
    for each in docs:
        pretty.pprint(each)
        print('--------------------')
except Exception as e:
    print("Oops")
