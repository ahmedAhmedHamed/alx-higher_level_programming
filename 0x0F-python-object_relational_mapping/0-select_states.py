#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    arguments = argv
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host='http://localhost:3306', user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT states FROM hbtn_0e_0_usa")

