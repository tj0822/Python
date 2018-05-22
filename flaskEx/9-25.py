from google.appengine.ext import ndb

class Product(ndb.Model):
    product_name = ndb.StringProperty()
    product_description = ndb.TextProperty()