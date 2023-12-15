#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time, write one
that is safe from MySQL injections!
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = db_connect.cursor()
    state_name = argv[4]
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                   (state_name,))
    data = cursor.fetchall()

    for row in data:
        print(row)

    db_connect.close()
