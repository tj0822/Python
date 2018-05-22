from datetime import datetime

from flask import Flask, request, render_template, redirect, url_for
from flask import MongoKit, Document

app = Flask(__name__)

class Task(Document):
    __collection__ = 'tasks'
    structure = {
        'title': unicode,
        'text': unicode,
        'creation': datetime,
    }
    required_fields = ['title', 'creation']
    default_values = {'creation': datetime.utcnow}
    use_dot_notation = True

db = MongoKit(app)
db.register([Task])