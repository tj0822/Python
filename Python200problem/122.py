#-*- coding:utf-8 -*-

listdata1 = [0, 1, 2, 3, 4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]
listdata4 = [1, 2, 3, 4]

print(all(listdata1))
print(all(listdata2))
print(all(listdata3))
print(all(listdata4))
print()
print(any(listdata1))
print(any(listdata2))
print(any(listdata3))
print(any(listdata4))

