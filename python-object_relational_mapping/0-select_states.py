#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def list_states(username, password, database):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
