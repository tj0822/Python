#-*- coding:utf-8 -*-

n = 10
my3 = (10, 20)[n<0]
print('my3 = ', my3)

# my1 = enumerate([10, 20, 30])
# print('my1 = ', my1)
# print('dict(my1) = ', dict(my1))
#
# my2 = zip([10, 20, 30], [100, 200, 300])
# print('my2 = ', my2)
# print('dict(my2) = ', dict(my2))

# num = 3
# my = {False:10, True:20}[num < 0]
# print(my)

# myData = [(1,10), (2,20), (3,30)]
# my = {k:v for k, v in myData}
# print(my)


#[리스트구성데이터 for 변수 in 반복가능데이터 if 판단문]

# myList = [n*10 for n in range(1,11)]
# print(myList)

# myList = [n for n in range(1,11) if n%2 == 0]
# print(myList)


#약수 구하기
# n =  int(input('n = '))
# yaksu = [i for i in range(1,n+1) if n%i==0]
# print(yaksu)
