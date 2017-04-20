# -*- coding: utf-8 -*-

import NaiveBayes
import csv
import os
import datetime

trainingSet = []
trainingSet.append({'wordList' : ['a', 'b', 'c', 'd']})

output_path = 'output_' + str(datetime.datetime.today().date())
os.mkdir(output_path)


f = open(output_path + '/test.csv', 'w')

cw = csv.writer(f, delimiter=',')
cw.writerow(trainingSet)
f.close()