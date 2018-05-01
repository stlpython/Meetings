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

conf = {
    '/': { 'tools.staticdir.root': "/srv/app/static" },
    '/static':
        {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "/srv/app/static"
        },
    '/favicon.ico':
        {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': "/srv/app/static/favicon.ico"
        },
    }

api_conf = {
    '/favicon.ico':
        {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': "/srv/app/static/favicon.ico"
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
    def r(self):
        import random
        return str(random.randint(9999, 99999))

    @cherrypy.expose
    def u(self):
        return "users"

    @cherrypy.expose
    def file(self):
        return """
        <html><h3>Upload a file</h3>
            <form action="/upload" method="post" enctype="multipart/form-data">
            Filename: <input type="file" name="myFile" />
            <input type="submit" /></form></html>
        """

    @cherrypy.expose
    def upload(self, myFile):
        out = """<html></pre>
            myFile length: %s<br />
            myFile filename: %s<br />
            myFile mime-type: %s
        </pre>
        </html>"""
        size = 0
        while True:
            data = myFile.file.read(8192)
            if not data:
                break
            size += len(data)
        return out % (size, myFile.filename, myFile.content_type)


class DistrolessDemo_API(object):
    @cherrypy.expose
    def index(self):
        return "This is the api"

    @cherrypy.expose
    def status(self):
        return "<html>Things are looking: Good </html>"

    @cherrypy.expose
    def r(self):
        import random
        return str(random.randint(9999, 99999))

    @cherrypy.expose
    def download(self):
        return "</html><h1>Download Things</h1></html>"

if __name__ == '__main__':
    cherrypy.tree.mount(DistrolessDemo(), '/', conf)
    cherrypy.tree.mount(DistrolessDemo_API(), '/api', api_conf)
    cherrypy.server.socket_host = host
    cherrypy.server.socket_port = port
    cherrypy.engine.start()
    cherrypy.engine.block()

