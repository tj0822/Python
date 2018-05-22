lemonism = Account.query(Account.userid == 6).get()
search5 = Account.query(Account.userid == 7).get()
gdhyun = Account.query(ancestor = ndb.Key(pairs=[
    (lemonism.key.kind(), lemonism.key.id()),
    (search5.key.kind(), search5.key.id())
]).fetch()