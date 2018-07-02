import os
import sys
lib = './libraries/'
if os.path.isdir(lib):
    for f in os.listdir(lib):
        if os.path.isfile(lib + f) and os.path.splitext(lib + f)[1].lower() == '.whl':
            sys.path.insert(1, lib + f)
import cherrypy

"""
Bind to all interfaces including IPv6 interfaces
"""
host = "::"
port = 8080

conf = {
    '/': { 'tools.staticdir.root': "/srv/app" },
    '/static':
        {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "static"
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
        return "<html><h1>Welcome to the Google Distroless Demo!</h1></html>"

    @cherrypy.expose
    def status(self):
        return '<html><h1 style="background-color:#aca;">Status: Green</h1></html>'

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
        output = """<html></pre>
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
        return output % (size, myFile.filename, myFile.content_type)


class DistrolessDemo_API(object):
    @cherrypy.expose
    def index(self):
        return "This is the api"

    @cherrypy.expose
    def r(self):
        import random
        return str(random.randint(9999, 99999))

if __name__ == '__main__':
    cherrypy.tree.mount(DistrolessDemo(), '/', conf)
    cherrypy.tree.mount(DistrolessDemo_API(), '/api', api_conf)
    cherrypy.server.socket_host = host
    cherrypy.server.socket_port = port
    cherrypy.engine.start()
    cherrypy.engine.block()

