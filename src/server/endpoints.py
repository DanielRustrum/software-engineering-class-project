import cherrypy

import api
from api import RequestHandler


api.init()

def init():
    api.group("user", User())
    api.group("entry", Entry())
    api.group("entry/group", Group())
    

class User(object):
    @api.endpoint
    def default(self,nill = ""):
        return "Hello"
    
    @api.endpoint
    def token(self):
        return "result"

    @api.endpoint
    def create(self):
        return "result"

    @api.endpoint
    def delete(self):
        return "result"
    
    @api.endpoint
    def settings(self):
        return "result"
    

class Entry(object):
    @api.endpoint
    def default(self):
        pass

    @api.endpoint
    def get(self, entry = ""):
        pass

    @api.endpoint
    def update(self, entry = "", modify = {}):
        pass

    @api.endpoint
    def create(self, entry = ""):
        pass

    @api.endpoint
    def delete(self, entry = ""):
        pass

class Group(object):
    @api.endpoint
    def default(self):
        pass

    @api.endpoint
    def create(self, tag = ""):
        pass

    @api.endpoint
    def add(self, tag = "", entry = ""):
        pass

    @api.endpoint
    def delete(self, tag = ""):
        pass

    @api.endpoint
    def remove(self, tag = "", entry = ""):
        pass

    @api.endpoint
    def get(self, tag = "", entry = ""):
        pass