#!/usr/bin/python3
"""
A Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = db_connect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    data = cursor.fetchall()
    for row in data:
        print(row)

    db_connect.close()
