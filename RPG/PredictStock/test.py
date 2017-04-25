# -*- coding: utf-8 -*-

a = [('한국', 'NNG'),
 ('카카오', 'NNG'),
 ('는', 'JX'),
 ('3', 'NR'),
 ('일', 'NNM'),
 ('경기도', 'NNP'),
 ('성남시', 'NNP'),
 ('카카오', 'NNG'),
 ('뱅크', 'NNP'),
 ('에서', 'JKM'),
 ('이사회', 'NNG'),
 ('를', 'JKO'),
 ('열', 'VV'),
 ('고', 'ECE'),
 ('카카오', 'NNG'),
 ('뱅크', 'NNP'),
 ('이사회', 'NNG'),
 ('의장', 'NNG'),
 ('에', 'JKM'),
 ('김', 'NNG'),
 ('주원', 'NNG'),
 ('한국', 'NNG'),
 ('투자', 'NNG'),
 ('금융', 'NNG'),
 ('지주', 'NNG'),
 ('사장', 'NNG'),
 ('을', 'JKO'),
 ('재', 'XPN'),
 ('선임', 'NNG'),
 ('하', 'XSV')]

tagList = ['NNG', 'VV', 'VA', 'VXV', 'UN']

def getWords(a):
    for w in a:
        if(tagList.__contains__(w[1])):
            yield w[0]
print(tagList)

words = getWords(a)
print(words)

for i in words:
    print(i)