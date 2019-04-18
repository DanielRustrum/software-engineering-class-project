import pyrebase

from settings import settingsManager
keys = settingsManager.getSettings()["dbkeys"]
database = pyrebase.initialize_app(keys).database()

#* Auth
def updateToken(uid):
    pass

def getToken(uid):
    pass

def modifyPassword(uid):
    pass

def getPassword(uid):
    pass    

#* Users
def createUser(uid, data):
    userData = {
        "settings": data["settings"],
        "username": data["username"]
    }
    authData = {
        "pass": data["password"],
        "token": "none"
    }

    database.child("users").child(uid).push(userData)
    database.child("auth").child(uid).push(authData)

def deleteUser(uid):
    database.child("users").child(uid).set(None)
    database.child("auth").child(uid).set(None)

def getSettings(uid):
    return database.child("users").child(uid).child("settings")

def modifySettings(uid, settings):
    database.child("users").child(uid).child("settings").set(settings)

def modifyUsername(uid, username):
    database.child("users").child(uid).child("username").set(username)

def getUsername(uid):
    return database.child("")


#* Entries
def createEntry(data):
    pass

def modifyEntry(eid):
    pass

def deleteEntry(eid):
    pass

#* Tags
def createTag(data):
    pass

def deleteTag(tid):
    pass

def addTag(tid, eid):
    pass

def removeTag(tid, eid):
    pass