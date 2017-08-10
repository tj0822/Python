# -*- coding: utf-8 -*-
import csv
import pandas as pd
import datetime
# fileName = 'output_2017-05-19/trainMatFile.csv'
# fileName = 'output_2017-05-19/vocaListFile.csv'
# fileName = 'output_2017-05-19/classListFile.csv'
# trainMatFilte = open(fileName, 'r', encoding='UTF-8')
# reader = csv.reader(trainMatFilte)#, delimiter=',')#, quotechar='|')
#
# print(len(list(reader)[0][3]))

import numpy as np
import operator

# i = [1, 0, 0, 2, 0, 1, 1, 1, 1, 0, 3, 0, 0, 0, 0, 2, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 2, 1, 1, 0, 1, 1, 3, 1, 1, 22, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 3, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 3, 1, 1, 2, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 2, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 6, 1, 1, 1, 0, 0, 1, 3, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 2, 0, 0, 1, 2, 0, 1, 1, 0, 0, 0, 4, 0, 2, 1, 0, 0, 1, 0, 0, 0, 0, 2, 1, 1, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0, 0, 1, 1, 1, 0, 1, 6, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 13, 2, 0, 0, 0, 1, 2, 2, 1, 0, 1, 3, 0, 5, 1, 0, 0, 0, 0, 1, 2, 0, 1, 0, 0, 3, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1, 0, 0, 5, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 0, 1, 4, 1, 0, 0, 1, 2, 0, 1, 1, 1, 1, 0, 1, 0, 1, 3, 0, 1, 0, 0, 0, 5, 0, 0, 0, 1, 2, 2, 1, 1, 0, 0, 17, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 4, 0, 1, 1, 4, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 2, 1, 0, 1, 1, 0, 1, 0, 2, 1, 5, 5, 1, 0, 0, 0, 1, 1, 0, 1, 1, 2, 13, 0, 3, 1, 1, 4, 0, 2, 0, 1, 1, 0, 1, 1, 1, 2, 0, 3, 1, 2, 1, 0, 1, 2, 3, 1, 0, 0, 1, 2, 0, 1, 1, 0, 2, 1, 2, 0, 3, 1, 1, 3, 13, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 2, 3, 2, 0, 0, 6, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 0, 1, 2, 1, 3, 1, 4, 1, 1, 0, 1, 0, 1, 1, 2, 0, 0, 1, 0, 0, 2, 1, 0, 1, 0, 2, 1, 6, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 0, 1, 1, 2, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 2, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 2, 1, 1, 1, 0, 1, 1, 0, 1, 3, 0, 1, 1, 1, 4, 2, 1, 1, 1, 14, 3, 2, 1, 1, 0, 7, 6, 1, 1, 1, 7]
# w = ['헤럴드', '경제', '민정', '기자', '모바일', '케이', '음식', '배달', '서비스', '발전', '업계', '경쟁', '치열', '음식점', '연계', '서비스', '전문', '서비스', '인기', '배달', '민족', '이하', '배민', '요기', '케이', '배달', '시장', '계속', '성장', '가도', '배달', '배민', '운영', '형제', '지난해', '매출액', '전년', '대비', '증가', '사상', '최대', '매출', '배민', '영업', '손실', '기록', '영업', '이익', '달성', '흑자', '전환', '성공', '업계', '요기', '배달', '매출', '전년', '대비', '이상', '급증', '민의', '기요', '운영', '코리아', '배달', '인수', '덩치', '배민', '위협', '회사', '점유율', '배민', '기도', '코리아', '번가', '마켓', '배달', '서비스', '운영', '시너지', '효과', '배민', '요기', '배달', '산맥', '케이', '배달', '시장', '최근', '대기업', '다국적', '기업', '경쟁', '양상', '최근', '카카오', '카카오', '주문', '서비스', '배달', '업계', '삼국지', '선언', '현재', '카카오', '주문', '치킨', '피자', '한식', '이즈', '브랜드', '음식', '주문', '가능', '카카오', '배달', '서비스', '경우', '이즈', '제외', '동네', '음식점', '배달', '수가', '제한', '지적', '카카오', '상반기', '배달', '민족', '기존', '배달', '업체', '제휴', '가능성', '마트', '지난달', '출시', '카카오', '장보기', '인접', '배송', '서비스', '마케팅', '강화', '배달', '시장', '인지도', '계획', '음식점', '연계', '배달', '전문', '서비스', '최근', '등장', '배달', '시장', '푸드', '플라이', '기존', '배달', '식당', '음식', '온라인', '모바일', '주문', '배달', '배달', '서비스', '현재', '서울', '강남', '서초', '마포', '양천', '서비스', '제공', '차량', '공유', '업체', '연내', '한국', '음식', '배달', '시장', '진출', '계획', '현재', '신규', '사업', '음식', '배달', '서비스', '출시', '전세계', '운영', '중이', '지난해', '국내', '법인', '설립', '소식', '화제', '코리아', '관계자', '현재', '한국', '서비스', '준비', '상반기', '정식', '서비스', '출시', '헤럴드', '경제', '무단', '전재', '배포', '금지']
#
#
#
# print(i[0].index(max(i[0])))
# print(max(i[0]))
# print(i[0][41])
# print(w[41])
# print(np.argmax(i[0]))
# print(w[np.argmax(i[1])])

# print(w.count('경제'))

# ws = set(w)
#
# dic = {}
# for word in ws:
#     # print(word, ' : ', w.count(word), '개')
#     dic.update({word : w.count(word)})
#
# n = 10
# listDic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)[:n]
#
# print(listDic)
#
# topNDic = {}
# for l in listDic:
#     topNDic.update({l[0] : l[1]})


# dic = {'정도': 1, '인터넷': 2, '적용': 1, '보이': 1, '영복': 1, '와중': 1, '사진': 1, '선보이': 2, '판매': 3, '기다리': 1, '그렇': 1, '사람': 1, '실업': 1, '동시': 1, '경제': 2, 'ㆍ내년': 1, '임직원': 1, '경쟁': 1, '컴백': 1, '신용': 8, '우량': 1, '고은': 1, '빠르': 1, '최근': 1, '개월': 2, '파격': 1, '국민': 1, '쏟아지': 1, '우대': 1, '처음': 1, '급여': 1, '금융사': 1, '직장인': 1, '은행원': 5, '받으': 1, '호기심': 1, '기대감': 1, '자사': 1, '마이너스': 1, '지급액': 1, '카카오': 4, '기자': 1, '현재': 1, '분위기': 1, '기대': 1, '시작': 1, '자체': 1, '설명': 1, '가운데': 1, '따르': 1, '수요': 1, '광화문': 1, '멈추': 1, '자기': 1, '한도액': 1, '시범': 1, '실제': 1, '일반': 1, '규정': 1, '증언': 1, '재개': 1, '서울': 2, '데이트': 1, '좋아지': 1, '번째': 2, '한도': 2, '사친': 1, '의견': 1, '금리': 5, '소속': 1, '임금': 1, '은행업': 1, '시중': 1, '재정비하': 1, '은행': 5, '만들': 1, '고대': 1, '조회': 1, '기업체': 1, '뉴스': 1, '영업': 1, '통장': 1, '관련': 1, '이달': 1, '후반': 1, '확대': 1, '일각': 1, '케이': 4, '뱅크': 8, '혜택': 2, '유리': 1, '대출': 10, '해보': 1, '감독': 1, '여사': 1, '하다': 1, '번가': 1, '서비스': 1, '후문': 1, '상향': 1, '재결합': 1, '여신': 1, '갈아타': 1, '한번': 1, '권형': 1, '준영': 1, '계좌': 1, '대비': 1, '즐기': 1, '중단': 1, '개시': 1, '독보적': 1, '결별': 1, '최대': 1, '때문': 2, '회사': 1}
# listdic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)[:10]
# print('listdic : ', listdic)


# print(sorted(zip(i[0], w), reverse=True)[:5])
# for l in reader:
#   print(len(l[0]))
#   print(len(l[2]))
  # for i in l:
  #   print(i)

# print(trainMatList[0][1])
# print(trainMatList[1])
# for l in trainMatList:
#   print(l)






'''list에서 dictionay에존재하는 단어 수 count하기 '''
# l = ['삼성', 'SK', 'GS', '테스트']
# d = ['삼성', 'LG', '로또', '카카오']
# print(l.index('테스트'))
#
# l = ['a', 'b', 'c', 'd']
# c = [5, 2, 5, 1]
#
# df = pd.DataFrame()
# df['Name'] = l
# df['Count'] = c
# print(df)
#
# df2 = pd.DataFrame(columns=df.columns)
# df2.append(df.copy())
# print(df2)

##  print([str(datetime.date.today())] * 10)

# l = [0, 0, 1]
#
# c = [str(datetime.date.today()), l]
# d = ['2017-08-11', [1, 1, 0]]
#
# print(c)
# print(d)
# print([c[0]] * len(c[1]))
# print(c[1])


df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df = df.append(df2, ignore_index= True)
print(df)