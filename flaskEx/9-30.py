from random import randrange
from google.appengine.ext import ndb

class WinningEntity(ndb.Model):
    winning_date = ndb.DateProperty(auto_add_now=True)
    winning_rank = ndb.IntegerProperty()
    winning_name = ndb.StringProperty()
    winning_email = ndb.StringProperty()
    winning_product = ndb.StringProperty()

app = Flask(__name__)