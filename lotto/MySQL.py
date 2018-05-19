#-*- coding:utf-8 -*-

import mysql.connector


id = 'python'
password = 'python'
host = '13.124.58.9'
db ='test'

def selectStmt(query = None):
    cnx = mysql.connector.connect(user=id, password=password, host=host, database=db)
    cursor = cnx.cursor()

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    cnx.close()

    return results


def insertStmt(query = None):
    cnx = mysql.connector.connect(user=id, password=password, host=host, database=db)
    cursor = cnx.cursor()
    try:
        rtn = cursor.execute(query)
    except:
        pass

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()


