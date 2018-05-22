lemonism_key = ndb.Key("Account", 4785074604081152)
lemonism = lemonism_key.get()
lemonism.key.delete()