#!/usr/bin/python3
'''this modules lists all cities
from the database hbtn_0e_0_usa'''
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = ('SELECT cities.name \
             FROM states \
             JOIN cities \
             ON cities.state_id = states.id \
             WHERE states.name = %s \
             ORDER BY cities.id')
    parameter = (sys.argv[4],)
    cur.execute(query, parameter)
    rows = cur.fetchall()
    print(', '.join(col for row in rows for col in row))
    cur.close()
    db.close()
