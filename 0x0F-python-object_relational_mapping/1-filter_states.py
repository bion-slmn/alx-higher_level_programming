#!/usr/bin/python3
'''this modules lists all states 1-filter_states.py
from the database hbtn_0e_0_usa'''
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name \
                LIKE BINARY "N%" ORDER BY id')
    [print(row) for row in cur.fetchall()]
