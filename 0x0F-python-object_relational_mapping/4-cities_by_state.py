#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = db_connect.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id\
                   ORDER BY id")
    data = cursor.fetchall()

    for row in data:
        print(row)

    db_connect.close()
