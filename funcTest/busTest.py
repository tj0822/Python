#-*- coding:utf-8 -*-

from urllib import request


apikey = "bDGgCnlmIRDbUvtMj97bcrvkFeHkO5RGE%2BtmBt7rH0pbmiOK8Z03p34ugDsUzOdmUFBzDhAb2mXKlYtnE7Ms8Q%3D%3D"

url = 'http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getCtyCodeList'
queryParams = '?'

request = request(url + queryParams)
print(request)
request.get_method = lambda: 'GET'
response_body = request.urlopen(request).read()
print(response_body)


