from google.appengine.ext import ndb

class Product(ndb.Model):
    product_warehouse_date = ndb.DateProperty()
    product_created = ndb.DateTimeProperty(auto_now_add=True)
    product_updated = ndb.DateTimeProperty(auto_now=True)