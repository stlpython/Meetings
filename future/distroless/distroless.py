#!/usr/bin/env python3

import os
import sys
lib = './libraries/'
if os.path.isdir(lib):
    for f in os.listdir(lib):
        if os.path.isfile(lib + f) and os.path.splitext(lib + f)[1].lower() == '.whl':
            sys.path.insert(1, lib + f)
import cherrypy

host = "::"
port = 8080

pwd = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
conf = {
    '/': { 'tools.staticdir.root': pwd },
    '/static':
        {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "static"
        },
    '/favicon.ico':
        {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': pwd + "static/favicon.ico"
        },
    }

api_conf = {
    '/favicon.ico':
        {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': pwd + "static/favicon.ico"
        },
}

class DistrolessDemo(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def status(self):
        return "running"

    @cherrypy.expose
    def u(self):
        return "users"

class DistrolessDemo_API(object):
    @cherrypy.expose
    def index(self):
        return "This is the api"

    @cherrypy.expose
    def status(self):
        return "running"

    @cherrypy.expose
    def download(self):
        return "download stuffs"

if __name__ == '__main__':
    cherrypy.tree.mount(DistrolessDemo(), '/', conf)
    cherrypy.tree.mount(DistrolessDemo_API(), '/api', api_conf)
    cherrypy.server.socket_host = host
    cherrypy.server.socket_port = port
    cherrypy.engine.start()
    cherrypy.engine.block()

