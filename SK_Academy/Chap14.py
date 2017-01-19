#-*- coding:utf-8 -*-
import sys

myList = [10, 20, 30]
myList1 = myList
# del(myList1)
print(sys.getrefcount(myList)-1)

a = 10000
b = 10000
print(sys.getrefcount(a)-1)