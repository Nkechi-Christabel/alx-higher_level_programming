#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = db_connect.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{:s}'\
                   ORDER BY id".format(argv[4]))
    data = cursor.fetchall()

    for row in data:
        print(row)

    db_connect.close()
