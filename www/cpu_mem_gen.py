#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import random
import socket
import thread
import time
from os import curdir, sep

PORT_NUMBER = 8080
def memory_gen():
    # generate memory load
    mload = []
    mload.append(' ' * 100 * 1000 * 1000) 
    time.sleep(1)

def htmlFormat(title, body):
    thread.start_new_thread(memory_gen, ())
    #Generate cpu load
    sorted([random.random() for i in range(300000)])
    return "<html>\n<head>\n<title>{0}</title>\n</head>\n<body><h1 align=\"center\">{1}</h1></body>\n</html>".format(title,body)
#This class will handles any incoming request from the browser 
class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        hn = socket.gethostname()
        #self.wfile.write("Hello World from " + socket.gethostname())
        self.wfile.write(htmlFormat("hostname: "+hn,"get response from: " + ip))
        return

try:
    #Create a web server and define the handler to manage the incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()

