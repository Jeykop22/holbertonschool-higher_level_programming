#!/usr/bin/python3
"""
    Script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states \
                WHERE cities.state_id = states.id \
                AND states.name= '{}' \
                ORDER BY id".format(state_name))
    cities = cursor.fetchall()

    for city in cities:
        print(city[1], end='')
        if cities.index(city) != len(cities) - 1:
            print(", ", end="")
        else:
            print()
    if not len(cities):
        print()

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities_by_state(username, password, database, state_name)
