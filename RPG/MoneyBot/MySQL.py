#-*- coding:utf-8 -*-

import mysql.connector

cnx = mysql.connector.connect(user='python', password='python',
                              host='13.124.46.173',
                              database='stock')
def selectStmt(query = None):
    cursor = cnx.cursor()
    query = ("SELECT * FROM STOCK_LIST ")

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    cnx.close()

    return results


def insertStmt(query = None):
    cursor = cnx.cursor()

    rtn = cursor.execute(query)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()


def insertStmt(conn = None, query = None):
    cursor = conn.cursor()
    rtn = cursor.execute(query)
    cursor.close()

