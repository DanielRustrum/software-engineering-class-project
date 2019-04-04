import cherrypy
from cherrypy._cpserver import Server

import endpoints

class FrontEnd(object):
    @cherrypy.expose
    def index(self):
        #* Angular Frontend
        return open("src/public/index.html")

if __name__ == "__main__":
    endpoints.init()
    cherrypy.quickstart(FrontEnd(), config="src/client.conf")
    
