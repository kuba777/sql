# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    #without unicode
    c.execute("SELECT firstname, lastname from employees")

    #fetchall() retrieves all records from query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1]


    #unicode
    # # use a for loop to iterate through the database, printing the results line by line
    # for row in c.execute("SELECT firstname, lastname from employees"):
    #     print row