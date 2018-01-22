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
