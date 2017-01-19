#-*- coding:utf-8 -*-

'''
    파이썬에서 제공하는 표준 자료구조 : 리스트, 튜플, 딕셔너리(사전), 셋(집합)

    * collections 모듈
    - deque(양쪽이 열려있는 큐구조)
    - defaultdict
    - Counter
    - namedtuple
    - OrderedDict

    * array 모듈 : 동일한 데이터 타입
    * heapq 모듈(heap 생성, heap 내부자료 접근..)
    * bisect 모듈(정렬된 상태로 요소를 추가, 중복값 처리)
    * Queue
    * struct
    * copy

    [ collection ]
    Counter : 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 함수
'''


import collections

print(collections.Counter(['aa', 'cc', 'dd', 'aa', 'bb', 'ee']))
print(collections.Counter({"가":3, "나":2, "다":4}))
print(collections.Counter(a=2, b=4, c=1))

container = collections.Counter()
print(container)

container.update("aabcdeffgg")
print(container)

container.update({'c':2, 'f':3})

print(container)


# Counter 접근하기
for n in "abdfeh":
    print('%s : %d' %(n, container[n]))


ct = collections.Counter("Hello Jenny")
ct['x'] = 0
print(ct)

print(list(ct.elements()))


# most_common(n) 사용하기 : 상위 n 개를 시퀀스로 만든다.
ct2 = collections.Counter()
with open('test.txt', 'rt') as f:
    for li in f:
        ct2.update(li.rstrip().lower())

for item, cnt in ct2.most_common(5):
    print('%s : %2d' %(item, cnt))

print(ct2.most_common())


# Counter 객체는 산술/집합 연산이 가능하다.
ct3 = collections.Counter(['a', 'b', 'c', 'b', 'd', 'a'])
ct4 = collections.Counter('aeroplane')

# print(ct3)
# print(ct4)

print(ct3+ct4)

# print(ct3-ct4)
#
# print(ct4-ct3)
#
# print(ct3 & ct4)

print(ct3 | ct4)


# defaultdict 메서드는 컨테이너를 초기화 만들때 default 값을 지정한다.

def default_aa():
    return "aa"


dic = collections.defaultdict(default_aa, n1 = '하이')
print(dic)
print([dic['n1']])

print(dic['n2'])