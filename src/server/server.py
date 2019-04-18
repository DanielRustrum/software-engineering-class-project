import cherrypy, os
from cherrypy._cpserver import Server

import endpoints

class FrontEnd(object):
    @cherrypy.expose
    def default(self, *args, **kwargs):
        if len(args) > 0:
            fileExtension = args[0].split(".")[1]
            allowedExtensions = ["js", "css", "ico", "img", "svg", "png"]
            if fileExtension in allowedExtensions:
                try:
                    return open("src/public/" + args[0])
                except:
                    return
        return open("src/public/index.html")

if __name__ == "__main__":
    endpoints.init()
    cherrypy.quickstart(FrontEnd())
    
