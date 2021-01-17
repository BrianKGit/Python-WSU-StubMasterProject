import pymongo

cString = "mongodb+srv://MongoBKWSU:MongoBKWSU@mongobkwsu-ljuj6.gcp.mongodb.net/test?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE"
#cString = "mongodb://localhost"
connection = pymongo.MongoClient(cString)
db = connection.EventTickets
Events = db.Event
Tickets = db.Tickets
Users = db.Users

db.Tickets.createIndex({eventID: 1})