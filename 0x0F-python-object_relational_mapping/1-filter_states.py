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
    cur.execute("SELECT name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for index, row in enumerate(rows):
        if re.search("^N", row[0]):
            print(f"({index + 1}, '{row[0]}')")
    cur.close()
    db.close()
