#!/usr/bin/python3
"""takes in arguments and displays all values in the states table"""


import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s;", (sys.argv[4],))
    [print(states) for states in cur.fetchall()]
