# deletes all tickets
import pymongo
import pprint
# cString = "mongodb+srv://om3705is:om3705ispassword@mongobkwsu-ljuj6.gcp.mongodb.net/test?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE"
connection = pymongo.MongoClient(cString)
# connection = pymongo.MongoClient("mongodb://localhost")
db = connection.EventTickets
Tickets = db.Tickets

doc = Tickets.find()

# delets tickets one by one
# for each in doc:
#     Tickets.delete_one(each)
#     print('*')

# prints out what is left... if anything
doc3 = Tickets.find()
for each in doc3:
    prettyText = pprint.pformat(each, indent=4)
    print(prettyText)
