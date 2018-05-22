from flask import Flask
from werkzeug import Request

class HTTPMethodOverrideMiddleware(object):
    allowed_methods = frozenset([
        'GET',
        'HEAD',
        'POST',
        'DELETE',
        'PUT',
        'TRACE',
        'CONNECT',
        'OPTIONS'
    ])
    bodyless_methods = frozenset(['GET', 'HEAD', 'OPTIONS', 'DELETE', 'TRACE', 'CONNECT'])

    def __init__(self, app, input_name='_method'):
        self.app = app
        self.input_name = input_name

    def __call__(self, environ, start_response):
        request = Request(environ)

        if self.input_name in request.values:
            method = request.values[self.input_name].upper()

            if method in self.allowed_methods:
                method = method.encode('ascii', 'replace')
                environ['REQUEST_METHOD'] = method
            if method in self.bodyless_methods:
                environ['CONTENT_LENGTH'] = '0'

        return self.app(environ, start_response)

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

@app.route("/middleware", methods=["GET"])
def middleware_test_get():
    return """<html>
    <body>
        <form method="POST">
            <input type="hidden" name="_method" value="PUT">
            <input type="submit" value="PUT 전송 테스트">
        </form>
    </body>
    </html>"""

@app.route("/middleware", methods=["PUT"])
def middleware_test_put():
    return "이 메서드는 PUT 메서드로 호출되었습니다."

if __name__ == "__main__":
    app.run()