#-*- coding:utf-8 -*-

# parser.py
import requests
from bs4 import BeautifulSoup
import urllib

LOGIN_INFO = {'username' : 'admin', 'password' : ''}
# LOGIN_INFO = {'username' : 'tj0822', 'password' : ''}
# LOGIN_URL = 'http://www.jungol.co.kr/bbs/login_check.php'
LOGIN_URL = 'https://snubhlm.diversilab.com/index.php'

# Session 생성
s = requests.Session()

login_req = s.post(url = LOGIN_URL, data = LOGIN_INFO)
print(login_req.text)

# target_url = 'http://www.jungol.co.kr/theme/jungol/contest.php?bo_table=contest'
target_url = 'https://snubhlm.diversilab.com/index.php?m=analysis&tab=1'
soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
print(soup)

# for item in soup.find_all('td'):
#     print(item.text)
