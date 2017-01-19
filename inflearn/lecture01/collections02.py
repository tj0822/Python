#-*- coding:utf-8 -*-

# Deque : 양방향 큐(데크)는 컨테이너 양쪽 (앞뒤)에 아이템을 넣거나 뺄 수 있다.

import collections

deq = collections.deque("Hello python")

print(deq)
print(len(deq))

print(deq[0])

print(deq[-1])

deq.remove('o')
print(deq)

deq.append('k')
print(deq)

deq.appendleft('k')
print(deq)

deq.extendleft('d')
print(deq)


# 아이템 꺼내기
while True:
    try:
        print(deq.pop(), end=' ')
    except IndexError:
        break


while True:
    try:
        print(deq.popleft(), end=' ')
    except IndexError:
        break