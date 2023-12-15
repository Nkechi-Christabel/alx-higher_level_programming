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

    state_name = argv[4]
    query = "SELECT cities.name FROM cities " \
            "INNER JOIN states ON cities.state_id = states.id " \
            "WHERE states.name = %s ORDER BY cities.id"

    cursor.execute(query, (state_name,))
    data = cursor.fetchall()

    print(', '.join(city[0] for city in data))

    db_connect.close()
