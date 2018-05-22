from datetime import date
from flask import flask

app = Flask(__name__)

@app.template_filter('korean_date')
def datetime_convert(date):
    if isinstance(date, datetime.date):
        return date.strftime("%Y-%m-%d")
    else:
        return date