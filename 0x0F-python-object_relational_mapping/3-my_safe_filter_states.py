#!/usr/bin/python3
'''this modules lists all states from the database hbtn_0e_0_usa
 where name matches the argument.'''
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    stateName = (sys.argv[4],)
    query = ('SELECT * FROM states WHERE name = %s ORDER BY states.id')
    cur.execute(query, stateName)
    rows = cur.fetchall()
    for row in rows:
        print(row)
