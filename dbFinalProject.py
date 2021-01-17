import pymongo
import pprint
import sys

#print the version of python running on this device
#print(sys.version)

#connection = string to connect Mongo Atlas
#db = EventTickets is the name of the DB we are using store that in
#Event = a collection in EventTickets DB
#pp is used to print data in a nice pretty format
#eventResults stores all documents in Event
connection = pymongo.MongoClient("mongodb+srv://MongoBKWSU:Spring2019Databass@mongobkwsu-ljuj6.gcp.mongodb.net/test?retryWrites=true")
#connection = pymongo.MongoClient("mongodb://localhost")
db = connection.EventTickets
event = db.Event
tickets = db.Tickets
users = db.Users
pp = pprint.PrettyPrinter(indent=4)
eventResults = event.find()
ticketResults = tickets.find()
userResults = users.find()

#for loop to print all docs in Event in pretty format
for entry in eventResults:
    pp.pprint(entry)
    
print()
    
#for loop to print all docs in Event in pretty format
for entry in ticketResults:
    pp.pprint(entry)
    
print()

#for loop to print all docs in Event in pretty format
for entry in userResults:
    pp.pprint(entry)
    
