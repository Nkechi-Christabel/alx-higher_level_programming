#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    with MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    ) as db_connect:
        cursor = db_connect.cursor()
        cursor.execute(
            "SELECT states.name, cities.id, cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY id"
        )
        data = cursor.fetchall()

        for row in data:
            print("{}: ({}) {}".format(row[0], row[1], row[2]))
