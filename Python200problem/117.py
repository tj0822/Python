#-*- coding:utf-8 -*-

namelist = ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']


ret1 = sorted(namelist)
ret2 = sorted(namelist, reverse=True)

print(namelist)
print(ret1)
print(ret2)


namelist.sort()
print(namelist)


