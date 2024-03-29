#!/usr/bin/python3
"""lists all cities from the database, take 3 arguments:
    mysql username, mysql password and database name"""


import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id")
    [print(cities) for cities in cur.fetchall()]
