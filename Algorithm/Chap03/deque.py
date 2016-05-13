#-*- coding:utf-8 -*-

from collections import deque

que = deque([])
que.append('One')
que.append('Two')
print('que : ' + str(que))
print(que.popleft())

que.append('Three')
print('que : ' + str(que))
print(que.popleft())
print('que : ' + str(que))
print(que.popleft())
print('que : ' + str(que))