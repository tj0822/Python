from google.appengine.ext import ndb

class WinningEntity(ndb.Model):
    winning_date = ndb.DateProperty(auto_now_add=True)
    winning_rank = ndb.IntegerProperty()
    winning_name = ndb.StringProperty()
    winning_email = ndb.StringProperty()
    winning_product = ndb.StringProperty()