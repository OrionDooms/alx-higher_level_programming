#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table of
database where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    LH = "localhost"
    PT = 3306
    UN = sys.argv[1]
    PW = sys.argv[2]
    BASE = sys.argv[3]
    arg = sys.argv[4]
    db = MySQLdb.connect(host=LH, port=PT, user=UN, passwd=PW, db=BASE)
    cur = db.cursor()
    """
    Execute select from table, find the name that matches the one
    from the argument.
    """
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(arg))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
