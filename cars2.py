# -*- coding: utf-8 -*-

# Update the quantity on two of the records, and then output all of the records from the
# table.
# import sqlite3

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE inventory SET Quantity = 231 WHERE Molde = 'one'")
    c.execute("UPDATE inventory SET Quantity = 1234 WHERE Molde = 'two'")

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()
    print "Make, Model, Qty"
    for r in rows:
        print r[0], r[1], r[2]
        #print "{:3} {:10} {:>}".format(r[0], r[1], r[2])