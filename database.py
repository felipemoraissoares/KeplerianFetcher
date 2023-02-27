# Script to save TLE's in MySQL Database

# Python Imports
import mysql.connector
import datetime


def to_database(df_tle):
    # Change '###' to your Database configuration
    connection = mysql.connector.connect(host="###",
                                         user="###",
                                         password="###",
                                         database="###")

    cursor = connection.cursor()

    current_time = datetime.datetime.now()

    # This is an example of Insert SQL
    # Change the SQL according to your requirements
    sql = "INSERT INTO tle (id_norad, datetime, line1, line2) VALUES (%s, %s, %s, %s)"
    val = (df_tle['NoradID'], current_time, df_tle['Line1'], df_tle['Line2'])

    cursor.execute(sql, val)
    connection.commit()

    print(cursor.rowcount, "details inserted")
    connection.close()
