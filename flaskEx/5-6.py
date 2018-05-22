from flask import Flask
from simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)