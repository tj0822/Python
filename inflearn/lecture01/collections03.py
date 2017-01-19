#-*- coding:utf-8 -*-

# namedtuple()

# aa = ("홍길동", 24, "남")
#
# print(aa)
#
# bb = ("강복녀", 21, "여")
#
# print(bb[0])
#
# for n in [aa, bb]:
#     print('%s은(는) %d세 %s성입니다.' %n)

import collections

Person = collections.namedtuple("Person", 'name age gender')
aa = Person(name="강길동", age=25, gender="남")
bb = Person(name="강복녀", age=21, gender="여")

for p in [aa, bb]:
    print('%s은(는) %d세 %s성입니다.' %p)

# OrderedDict : 자료의 순서를 기억하는 사전형 클래스
dic = {}
dic["서울"] = "두산"
dic["인천"] = "SK"
dic["대구"] = "삼성라이온즈"
dic["광주"] = "기아타이거즈"

for i, j in dic.items():
    print(i, j)


dic1 = collections.OrderedDict()
dic1["서울"] = "두산"
dic1["인천"] = "SK"
dic1["대구"] = "삼성라이온즈"
dic1["광주"] = "기아타이거즈"
print("------------------------")
for i, j in dic1.items():
    print(i, j)