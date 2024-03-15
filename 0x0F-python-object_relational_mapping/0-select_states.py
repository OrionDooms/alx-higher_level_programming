#!/usr/bin/python3
""" This script lists all states from the database"""
import MySQLdb
LH = "localhost"
PT = 3306
U = "root"
PW = "root"
BASE = "hbtn_0e_0_usa"
db = MySQLdb.connect(host=LH, port=PT, user=U, passwd=PW, db=BASE)
cur = db.cursor()
"""Execute select from states and sorted id in ascending order"""
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
