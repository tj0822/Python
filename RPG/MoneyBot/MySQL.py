#-*- coding:utf-8 -*-

import mysql.connector
import pandas as pd

id = 'python'
password = 'python'
host = '13.124.46.173'
db ='stock'

def selectStmt(query = None):
    cnx = mysql.connector.connect(user=id, password=password, host=host, database=db)
    cursor = cnx.cursor()

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    cnx.close()

    return results

#
def insertStmt(query = None):
    cnx = mysql.connector.connect(user=id, password=password, host=host, database=db)
    cursor = cnx.cursor()

    rtn = cursor.execute(query)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

def insertStmt(query = None):
    cnx = mysql.connector.connect(user=id, password=password, host=host, database=db)
    cursor = cnx.cursor()

    rtn = cursor.execute(query)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()


def insertStmt(query = None):
    cnx = mysql.connector.connect(user=id, password=password, host=host, database=db)
    cursor = cnx.cursor()

    rtn = cursor.execute(query)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()



# url = 'http://news.nate.com/view/20180120n08557?mid=n0301'
# query = "SELECT news_title, item_source, issueDatetime, text_characters, sentiment_targets, sentiment_document FROM aibril_alu WHERE url = '%s' " % url
#
# result = selectStmt(query)
# print(result)
# if result.__len__() == 0:
#     print('없음')
# else:
#     news_title = result[0][0]
#     item_source = result[0][1]
#     issueDatetime = result[0][2]
#     text_characters = result[0][3]
#     sentiment_targets = result[0][4]
#     sentiment_document = result[0][5]
#     print(news_title,item_source,issueDatetime,text_characters,sentiment_targets,sentiment_document)