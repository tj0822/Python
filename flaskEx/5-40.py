from flask import Flask
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)

cache = SimpleCache()

@app.route("/get_item")
def get_item():
    rv = cache.get('my-item')
    if rv is None:
        rv = calculate_value()
        cache.set('my-item', rv, timeout=5 * 60)
    return rv

def calcurate_value():
    return "calcurated value test"