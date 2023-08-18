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
    db = MySQLdb.connect(host='localhost',
                         port=3306, user=username, passwd=password, db=db_name)
    cur = db.cursor()
    query = ('SELECT cities.id, cities.name, states.name FROM states, cities'
             ' WHERE'
             ' states.id = cities.state_id'
             ' ORDER BY cities.id ASC')
    cur.execute(query)
    rows = cur.fetchall()
    for index, row in enumerate(rows):
        print(row)
    cur.close()
    db.close()
