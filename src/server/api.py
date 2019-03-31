import cherrypy

class RequestHandling(object):
    def __init__(self, requestType = "GET", needsAuth = False, *queryies):
        self.needsAuth = needsAuth
        self.requestType = requestType
        self.queries = queryies
        self.error = 0


    def __enter__(self)
        if self.error != 0:
            return {"Error": {}}
        elif len(self.queries) == 2:
            return self.queries[1]
        else:
            return {}

    def __exit__(self, type, value, traceback):
        pass


def APIendpoint(function):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def _(*args, **kwargs):
        return function(*args, **kwargs)
    return _

def APIfallback(function):
    @cherrypy.expose
    def _(*args, **kwargs):
        return function(*args, **kwargs)
    return _
