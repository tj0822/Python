qry = Account.query(ndb.AND(Account.username == 'Jihwan Lemonism Hyun',
                            ndb.OR(Account.email == 'lemonism@alphagirl.com',
                                   Account.userid == 1)))