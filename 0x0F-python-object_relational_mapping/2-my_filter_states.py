#!/usr/bin/python3
'''this modules lists all states from the database hbtn_0e_0_usa
 where name matches the argument.'''
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = ('SELECT * FROM states WHERE name = "{}"')
    cur.execute(query.format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
