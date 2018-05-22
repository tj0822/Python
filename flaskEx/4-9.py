>>> User.query.filter(User.name == 'admin').delete()
>>> db_session.commit()