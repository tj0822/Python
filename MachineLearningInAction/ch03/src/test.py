#-*- coding:utf-8 -*-
'''
Created on 2015. 10. 7.

@author: TaijinKim
'''

import trees
import treePlotter

from imp import reload
from numpy import size

# reload(trees)
# myDat, labels = trees.createDataset()
# print(myDat)
# trees.calcShannonEnt(myDat)
# myDat[0][-1] = 'maybe'
# trees.calcShannonEnt(myDat)

# a = [1, 2, 3]
# b = [4, 5, 6]
# a.append(b)labelCount
# print(a)

# reload(trees)
# myDat, labels = trees.createDataset()
# print(myDat)
# print(trees.splitDataSet(myDat, 0, 1))
# print(trees.splitDataSet(myDat, 0, 0))

# 데이터 분할 시 가장 좋은 속성 선택하기
# reload(trees)
# myDat, labels = trees.createDataset()
# trees.chooseBestFeatureSplit(myDat)

# 데이터 분할 시 가장 좋은 속성 선택하기(정보이득 구하지 않고 바로 엔트로피로 비교하기
# reload(trees)
# myDat, labels = trees.createDataset()
# trees.chooseBestFeatureSplit2(myDat)


# reload(trees)
# myDat, labels = trees.createDataset()
# myTree = trees.createTree(myDat, labels)
# print(myTree)


# myDat, labels = trees.createDataset()
# print(labels)
# myTree = treePlotter.retrieveTree(0)
# print(myTree)
# 
# trees.storeTree(myTree, 'classifierStorage.txt')
# trees.grabTree('classifierStorage.txt')


# reload(trees)
# reload(treePlotter)
fr = open('../data/lenses.txt')

lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']

lensesTree = trees.createTree(lenses, lensesLabels)
print(lensesTree)
treePlotter.createPlot(lensesTree)