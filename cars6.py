# -*- coding: utf-8 -*-
# Finally output the car’s make and model on one line, the quantity on another line, and
# then the order_dates on subsequent lines below that.

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT DISTINCT inventory.make, inventory.molde, orders.order_date, inventory.quantity FROM inventory, orders WHERE inventory.molde = orders.model")

    rows = c.fetchall()
   

    for r in rows:
        print "Make and model", r[0], r[1]
        print "Qty", r[3]
        print "Order date", r[2]
        print 