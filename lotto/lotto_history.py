#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import os
import lotto.MySQL as sql

# 로또 메인 페이지
mainUrl = 'http://www.nlotto.co.kr/common.do?method=main'
soup = BeautifulSoup(urllib.request.urlopen(mainUrl).read(), "lxml")

# 마지막 회차 조회
lastSeries = int(soup.find(id="lottoDrwNo").text)

def GetLottoHistoryToCsv():
    outputFileName = 'data/' + 'lotto_result' + '(1~' + str(lastSeries) + ')' + '.csv'

    if os.path.exists(outputFileName):
        # 생성된 파일이 있으면 pass
        pass
    else:
        #생성된 파일이 없으면 crawling
        with open(outputFileName, 'a') as f:
            for i in range(1, lastSeries+1):
                url = 'http://www.nlotto.co.kr/gameResult.do?method=byWin&drwNo=' + str(i)

                soup = BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")

                result = str(soup.find(id="desc")['content'])
                ret =  result.split('당첨번호')

                nubmerList = result.split('당첨번호')[1].split('.')[0].strip().split('+')[0].split((','))
                n1, n2, n3, n4, n5, n6 = nubmerList
                bonusNumber = result.split('당첨번호')[1].split('.')[0].strip().split('+')[1]
                totalCnt = result.split('당첨번호')[1].split('.')[1].split(('총'))[1].split(',')[0].strip().replace('명', '').replace(',', '')
                price = result.split('당첨번호')[1].split('.')[1].split(('총'))[1].split('당첨금액')[1].strip().replace('원', '').replace(',', '')

                print(str(i) + '회 당첨번호 :', nubmerList, '보너스 번호 :', bonusNumber, '1등 수 :', totalCnt, '인당 당첨금액 :', price)
                f.writelines(str(i) + ',' + n1 + ',' + n2 + ',' + n3 + ',' + n4 + ',' + n5 + ',' + n6 + ',' + bonusNumber + ',' + totalCnt + ',' + price + '\n')


def GetLottoHistoryToSQL():
    chkQuery = "SELECT series from lotto_history"
    chkResult = sql.selectStmt(chkQuery)
    chkList = []
    for row in chkResult:
        chkList.append(int(row[0]))
    crawlingList = list(set(list(range(1, lastSeries+1))) - set(chkList))

    if crawlingList.__len__() == 0:
        print('대상 없음')
        return

    for i in crawlingList:
        url = 'http://www.nlotto.co.kr/gameResult.do?method=byWin&drwNo=' + str(i)

        soup = BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")

        result = str(soup.find(id="desc")['content'])
        ret = result.split('당첨번호')

        nubmerList = ret[1].split('.')[0].strip().split('+')[0].split((','))
        n1, n2, n3, n4, n5, n6 = nubmerList
        bonusNumber = ret[1].split('.')[0].strip().split('+')[1]
        totalCnt = ret[1].split('.')[1].split(('총'))[1].split(',')[0].strip().replace('명','').replace(',', '')
        price = ret[1].split('.')[1].split(('총'))[1].split('당첨금액')[1].strip().replace('원','').replace(',', '')

        print(str(i) + '회 당첨번호 :', nubmerList, '보너스 번호 :', bonusNumber, '1등 수 :', totalCnt, '인당 당첨금액 :', price)
        query = "insert into lotto_history(series, n1, n2, n3, n4, n5, n6, bonus_n, total_winner, each_price, timestamp) VALUES (%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, NOW()) " % (int(i), int(n1), int(n2), int(n3), int(n4), int(n5), int(n6), int(bonusNumber), int(totalCnt), int(price))
        sql.insertStmt(query=query)

GetLottoHistoryToSQL()