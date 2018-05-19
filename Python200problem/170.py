#-*- coding:utf-8 -*-

from urllib.request import urlopen

url = 'http://www.nate.com'
with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)
