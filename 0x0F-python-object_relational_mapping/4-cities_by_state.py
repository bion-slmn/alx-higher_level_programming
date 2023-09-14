#!/usr/bin/python3
'''this modules lists all cities
from the database hbtn_0e_0_usa'''
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name \
                FROM states \
                JOIN cities \
                ON cities.state_id = states.id \
                ORDER BY cities.id')
    rows = cur.fetchall()
    for row in rows:
        print(row)
