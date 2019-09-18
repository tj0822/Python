#-*- coding:utf-8 -*-

import pymysql as mysql



id = 'tj0822'
password = 'jjin1226'
host = '192.168.0.5'
db ='t_data_platform'

def selectStmt(query = None):
    cnx = mysql.connect(user=id, password=password, host=host, database=db, cursorclass=mysql.cursors.DictCursor)
    cursor = cnx.cursor()

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    cnx.close()

    return results


def insertStmt(query = None):
    cnx = mysql.connect(user=id, password=password, host=host, database=db)
    cursor = cnx.cursor()
    try:
        # print(query)
        rtn = cursor.execute(query)
        # print(rtn)
    except:
        pass

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()


