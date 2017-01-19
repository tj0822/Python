#-*- coding:utf-8 -*-
import csv
from math import log

# 데이터 로드

def loadCsvData():
    listData = []

    data = open("../data/train.csv")
    csv_data = csv.reader(data)
    for row in csv_data:
        listData.append(row)
    data.close()

    return listData

listCsvData = loadCsvData()

# print(listCsvData[0])
print(listCsvData[0][1:94])
# print(len(listCsvData[0]))
#총 95개 컬럼, 1번째 id, 95번째 target, 나머지는 feat_1 ~ feat_93




# 주어진 속성으로 데이터 집합 분할하기
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            # print(reducedFeatVec)
            retDataSet.append(reducedFeatVec)
    return retDataSet

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCount = {}
    for featVec in dataSet:
        # print('featVec : ' + str(featVec))
        currentLabel = featVec[-1]
        # print('currentLabel : ' + currentLabel)

        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1
    shannonEnt = 0.0
    # print('labelCount : ' + str(labelCount))

    for key in labelCount:
        # print('key : ' + key)
        # print('labelCount[key]) : ' + str(labelCount[key]))
        prob = float(labelCount[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
        # print('prob : ' + str(prob))
        # print(shannonEnt)
    return shannonEnt

# 데이터 분할 시 가장 좋은 속성 선택하기
def chooseBestFeatureSplit(dataSet):
    numFeatures = len(dataSet[0]) - 2
    print('numFeatures : ' + str(numFeatures))
    baseEntropy = calcShannonEnt(dataSet)
    print('baseEntropy : ' + str(baseEntropy))
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(1, (numFeatures+1)):
        featList = [example[i] for example in dataSet]
        print('featList : ' + str(featList))
        uniqueVals = set(featList)
        # print('uniqueVals : ' + str(uniqueVals))
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    print(bestFeature)
    return bestFeature


# print(listCsvData[1:10])
chooseBestFeatureSplit(listCsvData)