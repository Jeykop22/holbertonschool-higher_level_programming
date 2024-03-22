#!/usr/bin/python3
"""
    Script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    Safe from MySQL injections
"""
import MySQLdb
import sys


def filter_states_by_name_safe(username, password, database, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()

    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(sql_query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_states_by_name_safe(username, password, database, state_name)
