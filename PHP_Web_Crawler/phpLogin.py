#-*- coding:utf-8 -*-

import urllib, urllib3
from http.cookiejar import CookieJar

username = 'tj0822'
password = ''

cj = CookieJar()

opener = urllib3.build_opener(urllib3.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'mb_id' : username, 'mb_password' : password})
opener.open('http://www.jungol.co.kr/bbs/login.php', login_data)
resp = opener.open('http://www.jungol.co.kr/theme/jungol/contest.php?cid=404')
print(resp.read())

