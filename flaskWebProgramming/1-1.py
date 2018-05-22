#-*- coding:utf-8 -*-

from wsgiref.simple_server import make_server

def applicaiton(environ, start_response):
    response_body = ['%s: %s' %(key, value) for key, value in sorted(environ.items())]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_header = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]
    start_response(status, response_header)

    return [response_body.encode("utf-8")]

httpd = make_server('localhost', 8051, applicaiton)
httpd.handle_request()