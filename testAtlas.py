import pymongo

try:
    connection = pymongo.MongoClient("mongodb+srv://MongoBKWSU:Spring2019Databass@mongobkwsu-ljuj6.gcp.mongodb.net/test?retryWrites=true")
    print('connected')
    db = connection.EventTickets
    Event = db.Event
    Tickets = db.Tickets
except Exception as connect:
    print('Connection failed', connect)


def showAllEvents():
    try:
        find = Event.find()
        for each in find:
            print(each)
    except Exception as searchAll:
        print('Search all failed', searchAll)
    

showAllEvents()