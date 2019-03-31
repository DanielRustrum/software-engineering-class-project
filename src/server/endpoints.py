import cherrypy

from api import APIendpoint as APIendpoint
from api import APIfallback as APIfallback
from api import RequestHandler as RequestHandler

def init():
    cherrypy.tree.mount(FrontEnd(), '/', 'src/client.conf')
    cherrypy.tree.mount(UserAPI(), '/api/user', 'src/api.conf')
    cherrypy.tree.mount(StorageAPI(), '/api/storage', 'src/api.conf')

# GUI
class FrontEnd(object):
    @cherrypy.expose
    def index(self):
        #* Angular Frontend
        return open("src/public/index.html")

# Rest API Endpoints
class UserAPI(object):
    @APIendpoint
    def getSettings(self):
        with RequestHandler(needsAuth = True) as result:
            return result  

class StorageAPI(object):
    @APIendpoint
    def getEntry(self):
        with RequestHandler(needsAuth = True) as result:
            return result