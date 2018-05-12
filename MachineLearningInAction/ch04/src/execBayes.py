#-*- coding:utf-8 -*-
'''
Created on 2015. 10. 18.

@author: KimTaeJin
'''
from numpy import *
from imp import reload
import bayes
import feedparser


# 전체 단어 집합(Set)중에 사용된 단어 count
# listOPosts, listClasses = bayes.loadDataSet()
# print(listOPosts)
# print(listClasses)
# myVocabList = bayes.createVocabList(listOPosts)
# print("myVocabList : " + str(myVocabList))
# print("listOPosts[0] : " + str(listOPosts[0]))
# bayes.setOfWords2Vec(myVocabList, listOPosts[0])
# bayes.setOfWords2Vec(myVocabList, listOPosts[3])
# print(listOPosts[3])
# print(bayes.setOfWords2Vec(myVocabList, listOPosts[3]))


# reload(bayes)
# listOPosts, listClasses = bayes.loadDataSet()
# print("listClasses : " + str(listClasses))
# myVocabList = bayes.createVocabList(listOPosts)
# print(myVocabList)
# trainMat = []
#
# for postinDoc in listOPosts:
#     trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
# print("trainMat : " + str(trainMat))
# p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)
# # print(pAb)
# print(p0V)
# print(p1V)


# reload(bayes)
# bayes.testingNB()


# mySent = 'This book is the best book on Python or M.L. I have ever laid eyes upon.'
# print(mySent.split())
# import re
# regEx = re.compile('\\W*')
# listOfTokens = regEx.split(mySent)
# print("listOfTokens : " + str(listOfTokens))
# print([tok.lower() for tok in listOfTokens if len(tok) > 0])



# import re
# regEx = re.compile('\\W*')
# emailText = open('../data/email/ham/6.txt').read()
# print("emailText : " + str(emailText))
# listOfTokens = regEx.split(emailText)
# print("listOfTokens : " + str(listOfTokens))



bayes.spamTest()





# import feedparser
# ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
# print(ny['entries'])
# print(len(ny['entries']))



# reload(bayes)
# ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
# sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
# print("ny : " + str(ny))
# print("sf : " + str(sf))
# vocabList, pSF, pNY = bayes.localWords(ny, sf)
# vocabList, pSF, pNY = bayes.localWords(sf, ny)


# reload(bayes)
# ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
# sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
# bayes.getTopWords(ny, sf)
