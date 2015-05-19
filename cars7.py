# -*- coding: utf-8 -*-
# Using the COUNT() function, calculate the total number of orders for each make and
# model.

# Output the car’s make and model on one line, the quantity on another line, and then
# the order count on the next line.

import sqlite3


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT make, model FROM orders")

    rows1 = c.fetchall()
    #print type(rows)

    make = []
    model = []

    for r in rows1:
        make.append(r[0])    
        model.append(r[1])

    a = list(set(model))

    a.sort()

    c.execute("SELECT DISTINCT orders.make, inventory.quantity, inventory.molde from orders, inventory WHERE inventory.molde = orders.model ORDER BY inventory.molde ASC")

    row = c.fetchall()

    #print row[1]
    count = 0

    #print a
    for r in a:
        c.execute("SELECT DISTINCT count(order_date) FROM orders WHERE model =" + "'" + r + "'" + "")
    
        row2 = c.fetchone()

        

        print "Make and model: ", row[count][0], row[count][2]
        print "Qty: ", row[count][1]
        print "# of orders: ", row2[0]
        print
        count = count + 1

    





    # for r in list(set(model)):
        

    #     c.execute("SELECT count(order_date) FROM orders WHERE model = " + "'" + r + "'")

    #     row2 = c.fetchone()
        
    #     print "make and model: ", row[0], row[2]
    #     print "qty: ", row[1]
    #     print "order count: ", row2[0]
    #     print



    
    # for r in list(set(make)):
    #     c.execute("SELECT count(order_date) FROM orders WHERE make = " + "'" + r + "'")

    #     results = c.fetchone()

    #     print r, results[0]
   