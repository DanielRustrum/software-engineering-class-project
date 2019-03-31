import cherrypy

from api import APIendpoint as APIendpoint
from api import APIfallback as APIfallback

def init():
    cherrypy.tree.mount(FrontEnd(), '/', 'src/client.conf')
    cherrypy.tree.mount(UserAPI(), '/api/user', 'src/api.conf')
    cherrypy.tree.mount(StorageAPI(), '/api/storage', 'src/api.conf')
    cherrypy.tree.mount(TokenAPI(), '/api/token', 'src/api.conf')

# GUI
class FrontEnd(object):
    @cherrypy.expose
    def index(self):
        #* Angular Frontend
        return open("src/public/index.html")

# Rest API Endpoints
class UserAPI(object):
    pass    

class StorageAPI(object):
    pass

class TokenAPI(object):
    pass