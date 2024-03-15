#!/usr/bin/python3
""" This script lists all states from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    LH = "localhost"
    PT = 3306
    U = sys.argv[1]
    PW = sys.argv[2]
    BASE = sys.argv[3]
    db = MySQLdb.connect(host=LH, port=PT, user=U, passwd=PW, db=BASE)
    cur = db.cursor()
    """Execute select from states and sorted id in ascending order"""
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
