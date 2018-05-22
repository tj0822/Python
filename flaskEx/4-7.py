>>> u = User.query.filter(User.name == 'admin').first()
<User u'admin'>
>>> print u.email
'admin@localhost'
>>> u.email = 'admin@jpub.co.kr'
>>> db_session.add(u)
>>> db_session.commit()