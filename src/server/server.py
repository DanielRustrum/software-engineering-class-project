import cherrypy
from cherrypy._cpserver import Server

import endpoints

#* Server Setup


if __name__ == "__main__":
    endpoints.init()
    cherrypy.quickstart()
    