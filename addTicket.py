# easily make and insert a ticket into EventTickets
import pymongo
import pprint
import random
cString = "mongodb+srv://MongoBKWSU:MongoBKWSU@mongobkwsu-ljuj6.gcp.mongodb.net/test?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE"
connection = pymongo.MongoClient(cString)
db = connection.EventTickets
Events = db.Event
Tickets = db.Tickets


class Ticket:

    # default constructor

    def __init__(self, eventID, section, seatNumber, price, sold):
        # self.id = id
        self.eventID = eventID
        self.section = section
        self.seatNumber = seatNumber
        self.price = price
        self.sold = sold

sections = ['A', 'B', 'C', 'D']
eventid = ['elvis', 'avengers', 'vikings', 'soundset', 'swan', 'paw', 'circus', 'twins', 'saints', 'godsmack', 'narnia', 'dolly', 'reagan', 'jefferies']
sold = [True, False]


#for x in range(1000):
#    newTicket = Ticket(random.choice(eventid), random.choice(sections), random.randrange(1, 200), random.randrange(30.00, 200.00), random.choice(sold))
#    tickAsDict = newTicket.__dict__
#    print(tickAsDict)    
#    try:
#        Tickets.insert_one(tickAsDict)
#        print('Ticket added')
#    except Exception as e:
#        print("Insert failed", e)

for each in eventid:
    
    price = 250
    
    for x in sections:
        
        price -= 50
        
        for y in range(1, 100, 1):
            
            newTicket = Ticket(each, x, y, price, random.choice(sold))
            tickAsDict = newTicket.__dict__
            print(tickAsDict)    
            try:
                Tickets.insert_one(tickAsDict)
                print('Ticket added')
            except Exception as e:
                print("Insert failed", e)

docs = Tickets.find()

pretty = pprint.PrettyPrinter(indent=4)
try:
    for each in docs:
        pretty.pprint(each)
        print('--------------------')
except Exception as e:
    print("Oops")
