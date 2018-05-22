from google.appengine.ext import ndb

class Account(ndb.Model):
  username = ndb.StringProperty()
  userid = ndb.IntegerProperty()
  email = ndb.StringProperty()