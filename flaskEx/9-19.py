lemonism = Account(username='Jihwan Lemonism Hyun', userid=6, email='delphi.jpub@
gmail.com')
lemonism.put()
gdhyun = Account(parent=lemonism.key, username='Gildong Hyun', userid=8,
email='gdhyun@lemonism.kr')
gdhyun.put()