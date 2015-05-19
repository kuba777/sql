# -*- coding: utf-8 -*-
# Add another table to accompany your “inventory” table called “orders”. This table
# should have the following fields: “make”, “model”, and “order_date”. Make sure to
# only include makes and models for the cars found in the inventory table. Add 15 records
# (3 for each car), each with a separate order date (YYYY-MM-DD).

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()


    c.execute("CREATE TABLE orders (make TEXT, model TEXT, order_date )")

    cars = [
            ('Ford', 'one', '2014-01-01'), 
            ('Ford', 'one', '2014-02-01'), 
            ('Ford', 'one', '2014-03-01'), 
            ('Ford', 'two', '2014-12-01'), 
            ('Ford', 'two', '2014-02-01'), 
            ('Ford', 'two', '2014-02-12'), 
            ('Ford', 'three', '2014-04-01'), 
            ('Ford', 'three', '2014-04-01'), 
            ('Ford', 'three', '2014-04-01'), 
            ('Honda', 'oneH', '2014-06-01'), 
            ('Honda', 'oneH', '2014-07-01'), 
            ('Honda', 'oneH', '2014-08-01'), 
            ('Honda', 'twoH', '2014-09-01'), 
            ('Honda', 'twoH', '2014-10-01'),     
            ('Honda', 'twoH', '2014-11-01'), 
            ]

    c.executemany("INSERT INTO orders VALUES (?, ?, ?)", cars)