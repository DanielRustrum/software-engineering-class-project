import cherrypy
import auth
from settings import settingsManager

class _ErrorHandler(object):
    def __init__(self):
        self.errorDictionary = settingsManager.getSettings()["error"]["errorManagement"]
        self.fallback = settingsManager.getSettings()["error"]["fallback"]

    def error(self, status, message, traceback, version):
        if status.split(" ")[0] in self.errorDictionary:
            cherrypy.response.headers["Content-Type"] = self.errorDictionary[status.split(" ")[0]]["type"]
            return self.errorDictionary[status.split(" ")[0]]["message"]
        cherrypy.response.headers["Content-Type"] = self.fallback["type"]
        return self.fallback["message"]

    def refresh(self):
        self.errorDictionary = settingsManager.getSettings()["error"]["errorManagement"]
        self.fallback = settingsManager.getSettings()["error"]["fallback"]

_errorHandler = _ErrorHandler()

class RequestHandler(object):
    def __init__(self, requestType = "GET", needsToken = False, successCode = 200):
        self.needsToken = needsToken
        self.requestType = requestType
        self.status = 200
    
    def __enter__(self):
        return [self._checkHandler("enter"), self.changeStatus]

    def __exit__(self, type, value, traceback):
        self._checkHandler("exit")
    
    def changeStatus(self, status):
        if not (status >= 200 and status < 300):
            self.status = status

    #* Private Methods
    def _checkHandler(self, type = ""):
        if type == "enter":
            if not self._checkRequest():
                return False
            if self.needsToken:
                return self._requestAuthorization()
            return True
        elif type == "exit":
            if self.status != 200:
                raise cherrypy.HTTPError(self.status)
        else:
            return True

    def _requestAuthorization(self):
        if "Authorization" in cherrypy.request.headers:
            authList = cherrypy.request.headers["Authorization"].split(" ")
            if authList[0] == "basic":
                userPass = authList[1].split(":")
            else:
                self.status = 400
                return False
        else:
            self.status = 400
            return False
        #! Authorize User
        return True

    def _checkRequest(self):
        return True

def endpoint(function):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def _(*args, **kwargs):
        return function(*args, **kwargs)
    return _

def init():
    refresh()
    cherrypy.config.update({
        'error_page.400': _errorHandler.error,
        'error_page.401': _errorHandler.error,
        'error_page.404': _errorHandler.error,
        'error_page.500': _errorHandler.error,
    })

def refresh():
    _errorHandler.refresh()