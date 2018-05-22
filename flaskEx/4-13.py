>>> con = engine.connect()
>>> con.execute(users.insert(), name='admin', email='admin@localhost’)