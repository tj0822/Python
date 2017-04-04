#-*- coding:utf-8 -*-
'''
Created on 2015. 10. 18.

@author: KimTaeJin
'''
from numpy import *


#4.1 벡터 함수의 단어 목록
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'postiong', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]   #1: 폭력적인, 0: 폭력적이지 않음
    return postingList, classVec


# 모듬 문서에 있는 모든 유일한 단어 목록을 생성(set)
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)         # | : 집합 유형 변수 합치기
    return list(vocabSet)


# 주어진 문서 내에 어휘 목록에 있는 단어가 존재하는지 아닌지를 표현하기 위해 어휘 목록, 문서 1과 0의 출력벡터 사용
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            # print "word : " + word
            returnVec[vocabList.index(word)] = 1
        else: print("the word: %s is not in my Vocabulary!" % word)
    # print("returnVec : " + str(returnVec))
    return returnVec

#4.2 나이브 베이스 분류기 훈련 함수
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    print("numTrainDocs : " + str(numTrainDocs))
    numWords = len(trainMatrix[0])
    print("numWords : " + str(numWords))
    print("trainCategory : " + str(trainCategory))
    print("sum(trainCategory) : " + str(sum(trainCategory)))
    print("float(numTrainDocs) : " + str(float(numTrainDocs)))
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    print("pAbusive : " + str(pAbusive))
    # p0Num = zeros(numWords)
    # p1Num = zeros(numWords)
    # p0Denom = 0.0
    # p1Denom = 0.0
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    print("range(numTrainDocs) : " + str(range(numTrainDocs)))
    for i in range(numTrainDocs):
        print("trainCategory[" + str(i) + "] : " + str(trainCategory[i]))
        if trainCategory[i] == 1:
            print("trainMatrix[" + str(i) + "] : " + str(trainMatrix[i]))
            p1Num += trainMatrix[i]
            print("p1Num : " + str(p1Num))
            p1Denom += sum(trainMatrix[i])
            print("p1Denom : " + str(p1Denom))
        else:
            print("trainMatrix[" + str(i) + "] : " + str(trainMatrix[i]))
            p0Num += trainMatrix[i]
            print("p0Num : " + str(p0Num))
            p0Denom += sum(trainMatrix[i])
            print("p0Denom : " + str(p0Denom))
    print("p1Num / p1Denom = " + str(p1Num) + "/" + str(p1Denom))
    print("p0Num / p0Denom = " + str(p0Num) + "/" + str(p0Denom))
    # p1Vect = p1Num / p1Denom   #log()로변경
    # p0Vect = p0Num / p0Denom   #log()로변경
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    print("p1Vect : " + str(p1Vect))
    print("p0Vect : " + str(p0Vect))
    return p0Vect, p1Vect, pAbusive


#4.3 나이브 베이스 분류 함수
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    # print("vec2Classify * p1Vec : " + str(vec2Classify * p1Vec))
    # print("vec2Classify * p0Vec : " + str(vec2Classify * p0Vec))
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    # print("p1 : " + str(p1))
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    # print("p0 : " + str(p0))
    if p1 > p0:
        return 1
    else:
        return 0
    
def testingNB():
    listOPosts, listClasses = loadDataSet()
    print(listClasses)
    print(listOPosts)
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        print(postinDoc)
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    print(trainMat)
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print("thisDoc : " + str(thisDoc))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print("thisDoc : " + str(thisDoc))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    

#4.4 나이브 베이스 중복 단어 모델
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


#4.5 파일 구문 분석과 전체 스팸 검사 함수
def textParse(bigString):
    import re
    # print("bigString : " + str(bigString))
    listOfTokens = re.split(r'\W*', bigString)
    # print("listOfTokens : " + str(listOfTokens))
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
    docList = []
    classList = []
    fullText = []
    for i in range(1, 20):
        # print("i : " + str(i))
        wordList = textParse(open('../data/email/spam/%d.txt' % i).read())
        # print('wordList : ', wordList)
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        # print(docList)
        # print(classList)
        wordList = textParse(open('../data/email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    print('docList : ', docList)
    print('classList : ', classList)

    vocabList = createVocabList(docList)
    trainingSet = list(range(50))
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []

    for docIndex in trainingSet:
        print('docIndex : ', docIndex)
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print('the error rate is :',float(errorCount) / len(testSet))


#4.6 RSS 피드분류기와 자주 발생하는 단어 제거 함수
def calcMostFreq(vocablist, fullText):
    import operator
    freqDict = {}
    for token in vocablist:
        freqDict[token] = fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse = True)
    return sortedFreq[:30]

def localWords(feed1, feed0):
    import feedparser
    docList = []
    classList = []
    fullText = []
    minLen = min(len(feed1['entries']), len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    top30Words = calcMostFreq(vocabList, fullText)
    for pairW in top30Words:
        if pairW[0]in vocabList: vocabList.remove(pairW[0])
    trainingSet = range(2*minLen)
    testSet = []
    for i in range(20):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print('the error rate is :', float(errorCount) / len(testSet))
    return vocabList, p0V, p1V



def getTopWords(ny, sf):
    import operator
    vocabList, p0V, p1V = localWords(ny, sf)
    topNY = []
    topSF = []
    for i in range(len(p0V)):
        if p0V[i] > -6.0:
            topSF.append((vocabList[i], p0V[i]))
        if p1V[i] > -6.0:
            topNY.append((vocabList[i], p1V[i]))
    sortedSF = sorted(topSF, key = lambda pair: pair[1], reverse=True)
    print("SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**")
    for item in sortedSF:
        print(item[0])
    sortedNY = sorted(topNY, key = lambda pair: pair[1], reverse=True)
    print("NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**")
    for item in sortedNY:
        print(item[0])