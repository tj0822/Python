from google.appengine.ext import ndb

class Product(ndb.Model):
    product_soldout = ndb.BooleanProperty()
    product_images = ndb.KeyProperty()
    register = ndb.UserProperty()

class ProductImages(ndb.Model):
    image_path = ndb.StringProperty()