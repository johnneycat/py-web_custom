
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import time, threading
from SocketServer import ThreadingMixIn


starttime = time.time()


class RequestHandler(BaseHTTPRequestHandler):
    def _writeHeaders(self, doc):
        if doc is None:
            self.send_response(404)
        else:
            self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _getdoc(self, filename):
        '''handle a request for a docment, returning one of two different pages as appropriate.'''
        global starttime
        print filename
        if filename == "/":
            return '''
            <html>
                <head>
                    <tittle>sample page</tittle>
                </head>
                <body>
                    this is a sample page,you can also look at the <a herf="status.html">server statistics</a>
                </body>
            </html>
            '''
        elif filename == "/status.html":
            return
            '''
            <html>
                <head>
                    <tittle>statistics</tittle>
                </head>
                <body>
                    this server has been running for %d seconds,
                </body>
            </html>
            ''' % int(time.time() - starttime)
        else:
            return None

    def do_HEAD(self):
        print 11111
        doc = self._getdoc(self.path)
        self._writeHeaders(doc)

    def do_GET(self):
        print 2222
        doc = self._getdoc(self.path)
        print doc
        print self.path
        self._writeHeaders(doc)
        if doc is not None:
            self.wfile.write(doc)
        else:
            self.wfile.write('''
            <html>
                <head>
                    <tittle>Not Found</tittle>
                </head>
                <body>
                <p>The request docment '%s' was not found</p>
                </body>
            </html>''' % self.path)

class ThreadingHttpServer(ThreadingMixIn, HTTPServer):
    pass

serveraddr = ('', 8765)
server = ThreadingHttpServer(serveraddr, RequestHandler)
server.serve_forever()