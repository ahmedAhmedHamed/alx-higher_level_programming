#!/usr/bin/python3
"""
this module houses 1-filter_states.py's solution
"""
import MySQLdb
from sys import argv
import re

if __name__ == "__main__":
    """
    connects to a database on localhost:3306
    and fetchest the names of all the states
    """
    arguments = argv
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name_searched = argv[4]
    db = MySQLdb.connect(host='localhost',
                         port=3306, user=username, passwd=password, db=db_name)
    cur = db.cursor()
    state_name_searched = state_name_searched.split(';', 1)[0]
    query = ('SELECT cities.name FROM states, cities'
             ' WHERE BINARY states.name = "{0}"'
             'AND states.id = cities.state_id'
             ' ORDER BY cities.id ASC').format(state_name_searched)
    cur.execute(query)
    rows = cur.fetchall()
    if len(rows) == 0:
        print()
    for index, row in enumerate(rows):
        if index == len(rows) - 1:
            print(row[0])
        else:
            print(row[0], end=', ')
    cur.close()
    db.close()
