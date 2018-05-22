from google.appengine.api import users

product_image = ProductImages(image_path="/path/to/image")
product_image.put()
product_apple = Product(product_soldout=False, product_images=product_image.key, register=users.get_current_user())
product_apple.put()