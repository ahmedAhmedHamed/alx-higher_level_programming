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
    query = ('SELECT id, name FROM states WHERE name = "{0}"'
             ' ORDER BY id ASC').format(state_name_searched)
    cur.execute(query)
    rows = cur.fetchall()
    for index, row in enumerate(rows):
        print(row)
    cur.close()
    db.close()
