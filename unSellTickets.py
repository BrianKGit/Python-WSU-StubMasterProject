# switches sold tickets back to unsold
# clears users history
import pymongo

try:
    cString = 'mongodb+srv://om3705is:om3705ispassword@mongobkwsu-ljuj6.gcp.mongodb.net/t' + \
        'est?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE'
    connection = pymongo.MongoClient(cString)
    # connection = pymongo.MongoClient("mongodb://localhost")
    print('connected')
    db = connection.EventTickets
    Tickets = db.Tickets
    Users = db.Users
except Exception as connect:
    print('Connection failed', connect)


# sets all tickets in tickets db to unsold
def unSell():
    try:
        lookFor = {'sold': True}
        changeTo = {"$set": {'sold': False}}
        Tickets.update_many(lookFor, changeTo)
    except Exception as e:
        print("Failed to update", e)


# removes history from user
def wipeHistory():
    try:
        users = Users.find()
        for each in users:
            Users.update_one(each, {'$unset': {'tickets': 1}})
    except Exception as d:
        print('Delete failed', d)


unSell()
wipeHistory()
