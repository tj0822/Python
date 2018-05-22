lemonism_key = ndb.Key("Account", 5629499534213120)
lemonism = lemonism_key.get()
lemonism.username = "Linus Torvalds"
lemonism.userid = 4
lemonism.email = "linus@google.com"
lemonism.put()