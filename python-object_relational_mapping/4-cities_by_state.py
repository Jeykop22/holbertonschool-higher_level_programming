#!/usr/bin/python3
"""
    Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities_by_state(username, password, database):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                   JOIN states ON cities.state_id = states.id ORDER BY \
                   cities.id ASC")
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities_by_state(username, password, database)
