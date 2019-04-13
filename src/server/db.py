import pyrebase

from settings import settingsManager

firebase = pyrebase.initialize_app(settingsManager.getSettings["dbkeys"])


#* Users
def createUser(data):
    pass

def deleteUser(id):
    pass

def 


#* Entries
def createEntry(id):
    pass

def modifyEntry(id):
    pass

def deleteEntry(id):
    pass