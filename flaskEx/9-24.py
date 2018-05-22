from google.appengine.ext import ndb

class Product(ndb.Model):
    product_id = ndb.IntegerProperty()
    product_view_cnt = ndb.FloatProperty()