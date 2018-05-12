#-*- coding:utf-8 -*-
import RPG.MoneyBot.MySQL as sql
import datetime
import pandas as pd

def GetPortfolio(self):
    return {'006400'}

def GetStockByAibrilScore(date = None):
    query = " SELECT AA.STOCK_CODE, (AA.sentiment_targets + AA.sentiment_document)/2 " \
          "   FROM ( SELECT A.*, @curRank := @curRank + 1 AS RANK " \
          "            FROM (SELECT STOCK_CODE, AVG(sentiment_targets) sentiment_targets, AVG(sentiment_document) sentiment_document " \
          "                    FROM aibril_alu " \
          "                   WHERE issueDatetime >= '%s' " \
          "                     AND issueDatetime < '%s' 	" \
          "                GROUP BY STOCK_CODE) A, (SELECT @curRank := 0) r" \
          "                ORDER BY A.sentiment_targets DESC) AA" \
          " WHERE AA.RANK <= 1 " %(pd.to_datetime(str(date + datetime.timedelta(days=-1)) + ' 15:30:00'), pd.to_datetime(str(date) + ' 15:30:00'))
    return sql.selectStmt(query)


GetStockByAibrilScore(datetime.datetime.strptime(str('2017-01-01'), "%Y-%m-%d").date())

