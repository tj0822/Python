# -*- coding: utf-8 -*-
import csv

# fileName = 'output_2017-05-19/trainMatFile.csv'
# fileName = 'output_2017-05-19/vocaListFile.csv'
# fileName = 'output_2017-05-19/classListFile.csv'
# trainMatFilte = open(fileName, 'r', encoding='UTF-8')
# reader = csv.reader(trainMatFilte)#, delimiter=',')#, quotechar='|')
#
# print(len(list(reader)[0][3]))

import numpy as np

l = [1, 4, 3, 2, 5, 7, 5]

print(np.argmin(l))
print(np.argmax(l))



# for l in reader:
#   print(len(l[0]))
#   print(len(l[2]))
  # for i in l:
  #   print(i)

# print(trainMatList[0][1])
# print(trainMatList[1])
# for l in trainMatList:
#   print(l)