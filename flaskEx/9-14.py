email_or_userid = ndb.OR(Account.email == 'lemonism@alphagirl.com', Account.userid == 1)
username_and_email = ndb.AND(Account.username == 'Jihwan Lemonism Hyun', email_or_userid)
qry = Account.query(username_and_email)