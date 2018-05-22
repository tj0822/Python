from datetime import date
from flask import flask

app = Flask(__name__)

@app.template_filter('korean_date')
def datetime_convert(date, date_format=None):
    format_string = "%Y-%m-%d"
    if date_format:
        format_string = date_format

    if isinstance(date, datetime.date):
        return date.strftime(format_string)
    else:
        return date