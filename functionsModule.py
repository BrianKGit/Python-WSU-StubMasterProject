# file to write out functions
import pymongo
import createUser
import hashlib
import uuid
# -----------------------------------------------------------------------------------------------
# Connection stuff
try:
    cString = 'mongodb+srv://om3705is:om3705ispassword@mongobkwsu-ljuj6.gcp.mongodb.net/t' + \
        'est?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE'
    connection = pymongo.MongoClient(cString)
    # connection = pymongo.MongoClient("mongodb://localhost")
    print('connected')
    db = connection.EventTickets
    Events = db.Event  # remember to change to Event for atlas and Events for local
    Tickets = db.Tickets
    Users = db.Users
except Exception as connect:
    print('Connection failed', connect)
# ------------------------------------------------------------------------------------------------


def showCurrentTickets(user):
    print('Here are your tickets dude')
    # in some window, a button will show upcoming tickets that user has


def addToTicketArray(ticketID):
    doc = Tickets.find_one({'_id': ticketID})
    return doc


def toUserHistory(ticketsArray, user):
    # look up user by Username
    # add ticketsArray to users history
    try:
        lookFor = {'_id': user}
        for each in ticketsArray:
            changeTo = {'$push': {'tickets': each}}
            Users.update_one(lookFor, changeTo)
        # changeTo = {"$push": {'tickets': ticketsArray}}
        # Users.update_one(lookFor, changeTo)
    except Exception as e:
        print("Failed to update", e)


def unSell():
    try:
        lookFor = {'sold': True}
        changeTo = {"$set": {'sold': False}}
        Tickets.update_many(lookFor, changeTo)
        print('unsold')
    except Exception as e:
        print("Failed to update", e)


def getVenue(id):
    try:
        doc = Events.find_one({'_id': id})
        print(doc)
        venue = doc.get('location').get('venue')
        print('\t' + venue)
    except Exception as m:
        print('couldnt get venue', m)
        return 'blank'
    return str(venue)


def showAllEvents():
    try:
        find = Events.find()
    except Exception as searchAll:
        print('Search all failed', searchAll)
    return find


def searchTickets(id):
    try:
        find = Tickets.find({'eventID': id, 'sold': False})
    except Exception as b:
        print('Ticket search Failed', b)
    return find


def setTicketToSold(e):
    # print before
    targetTicket = db.Tickets.find_one({'_id': e})
    print(targetTicket)
    print('....................')
    lookfor = {'_id': e}
    changeTo = {'$set': {'sold': True}}
    Tickets.update_one(lookfor, changeTo)
    # print after
    targetTicket = db.Tickets.find_one({'_id': e})
    print(targetTicket)
    # to do....ad this ticket to user history


def searchSpecificEventLocation(key, entry):
    try:
        myKey = 'location.' + key
        findEvent = Events.find({myKey: {'$regex': entry, '$options': 'i'}})
    except Exception as v:
        print('Search type failed', v)
    return findEvent


def searchSpecificEventType(key, entry):
    try:
        myKey = 'category.' + key
        findEvent = Events.find({myKey: {'$regex': entry, '$options': 'i'}})
    except Exception as v:
        print('Search type failed', v)
    return findEvent


# print(searchSpecificEventType('type', 'Music'))
# print(searchSpecificEventLocation('city', "Las Vegas"))


def searchSpecificEvent(key, entry):
    try:
        key = key
        print(key)
        entry = entry
        print(entry)
        # findEvent = Events.find({key: entry})
        # findEvent = Events.find({key: {'$regex': '^' + entry}})
        findEvent = Events.find({key: {'$regex': entry, '$options': 'i'}})
    except Exception as b:
        print('Events search Failed', b)
    return findEvent

# -------------------------------------------------------------------------------------------------
# formatting output


def eventHeader():
    eh = ''
    eh += 'ID' + '\t\t'
    eh += 'Event' + '\t\t\t'
    eh += 'Location'
    return eh


def eventFormat(dict):
    toS = '-------------------------------------------------------------------------------\n'
    toS += str(dict.get('_id')) + '\t\t'
    toS += str(dict.get('name')) + '\t\t\t'
    toS += str(dict.get('location').get('city')) + '\n\t\t'
    toS += str(dict.get('time')) + '\t\t\t'
    toS += str(dict.get('location').get('venue'))
    return toS


def ticketHeader():
    ts = ''
    ts += 'Event' + '\t\t'
    ts += 'Price' + '\t'
    ts += 'Section' + '\t    '
    ts += 'Seat' + '\t\t'
    ts += '#' + '\t'
    ts += '\n'
    return ts


def ticketFormat(dict):
    toString = ''
    toString += str(dict.get('eventID')) + '\t\t'
    toString += '$' + str(dict.get('price')) + '\t'
    toString += str(dict.get('section')) + '\t    '
    toString += str(dict.get('seatNumber')) + '\t'
    # toString += str(dict.get('sold'))
    # print(toString)
    return toString

# ----------------------------------------------------------------------------------------------
# user login stuff


# this one just looks to see if user already exists
def notTaken(pullUser):
    try:
        nameInDb = Users.find_one({'_id': pullUser})
        if nameInDb is None:
            print('Not taken yet')
            return True
        else:
            print('Already taken')
            return False
    except Exception as t:
        print('Failed to look for user', t)


# compares entered pass with db pass
def comparePassword(user, password):
    print('Verifying password.........')
    try:
        me = Users.find_one({'_id': user})
        userSalt = me.get('password').get('salt')
        userHash = me.get('password').get('hash')
        # print('\tFrom db: ' + str(userPassword) + '\n\tEntered: ' + str(password))
        hash = hashlib.sha512((password + userSalt).encode('utf-8')).hexdigest()
        if userHash == hash:
            print('Successful password login')
            return True
        else:
            print('Password did not match')
            return False
    except Exception as p:
        print('Password failed', p)
        return False


# finds user and checks password
def verifyUser(pullUser, pullPass):
    print('Looking for ' + pullUser)
    try:
        nameInDb = Users.find_one({'_id': pullUser})
        if nameInDb is None:
            print('Not found')
            return False

        else:
            print('Found!')
            print(nameInDb)
            return comparePassword(pullUser, pullPass)
    except Exception as m:
        print('Failed to find user', m)
        return False


# after checking username exists and passwords match then create new user
def createNewUser(id, name, password):
    # salt and hash ======================================================
    salt = uuid.uuid4().hex
    hash = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()
    passwordObject = createUser.password(salt, hash)
    # ====================================================================
    pObject = passwordObject.__dict__
    new = createUser.newUser(id, name, pObject)
    addUserToDatabase = new.__dict__
    print(addUserToDatabase)

    try:
        Users.insert_one(addUserToDatabase)
        print('User added')
    except Exception as e:
        print("Insert user failed", e)


def showUserPurchases(user):
    ticketString = ''
    ticketString += ticketHeader() + '\n'
    ticketString += '--------------------------------------------------------------------------\n'
    me = Users.find_one({'_id': user})
    tickets = me.get('tickets')
    for each in tickets:
        ticketString += ticketFormat(each)
        ticketString += '\n'

    return ticketString


# showUserPurchases('box12')
