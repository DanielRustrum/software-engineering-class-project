import cherrypy

import api
from api import RequestHandler


api.init()

def init():
    api.group("user", User())
    

class User(object):
    @api.endpoint
    def default(self,nill = ""):
        return "Hello"
    
    @api.endpoint
    def result(self):
        return "result"