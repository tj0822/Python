#-*- coding:utf-8 -*-


import os
import sys
import urllib.request
client_id = "DQQJq5hcdjisgmF_xkgJ"
client_secret = "vfS1jgkGo1"
encText = urllib.parse.quote("상계로 69-1")
url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)