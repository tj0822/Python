>>> r = users.select(users.c.id == 1).execute().first()
>>> r['name']