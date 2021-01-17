# file to write out functions
import pymongo

try:
    #cString = "mongodb+srv://MongoBKWSU:MongoBKWSU@mongobkwsu-ljuj6.gcp.mongodb.net/test?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE"
    cString = "mongodb://localhost"
    connection = pymongo.MongoClient(cString)
    print('connected')
    db = connection.EventTickets
    Events = db.Events
    Tickets = db.Tickets
except Exception as connect:
    print('Connection failed', connect)


def sort():
    return 'hi'


def showAllEvents():
    try:
        find = Events.find()
    except Exception as searchAll:
        print('Search all failed', searchAll)
    return find


def searchTickets(key):
    try:
        find = Tickets.find({key, entry})
    except Exception as b:
        print('Ticket search Failed', b)
    return find


def searchEvents(key, entry):
    try:
        key = key
        entry = entry
        commandStr = '{\'' + key + '\': \'' + entry + '\'}'
        print(commandStr)
        findEvent = Events.find(commandStr)
    except Exception as b:
        print('Events search Failed', b)
    return findEvent


def formatEvents(dict):
    toString = '\"' + dict.get('name') + '\"' + '  '
    toString += dict.get('location').get('venue') + '  '
    toString += dict.get('location').get('city') + ', '
    toString += dict.get('location').get('state') + '\n'
    toString += ('time needs format still...')
    print(dict)
    return toString
