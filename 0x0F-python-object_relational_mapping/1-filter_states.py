#!/usr/bin/python3
"""
This script lists all states and find all names that started with N
from the database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    LH = "localhost"
    PT = 3306
    UN = sys.argv[1]
    PW = sys.argv[2]
    BASE = sys.argv[3]
    db = MySQLdb.connect(host=LH, port=PT, user=UN, passwd=PW, db=BASE)
    cur = db.cursor()
    """
    Execute select from states, find all names that started with N and
    sorted id in ascending order
    """
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
