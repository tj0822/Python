>>> u = collection.User.find_one({name: 'admin'})
>>> u['email'] = u'admin@admin.kr'
>>> u.save()