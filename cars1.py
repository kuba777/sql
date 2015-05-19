# -*- coding: utf-8 -*-

#Using the “inventory” table from the previous homework assignment, add ( INSERT )
#5 records (rows of data) to the table. Make sure 3 of the vehicles are Fords while the
#other 2 are Hondas. Use any model and quantity for each.

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [
            ('Ford','one',10),
            ('Ford', 'two', 100),
            ('Ford', 'three', 50),
            ('Honda','oneH',25),
            ('Honda', 'twoH',35)]

    c.executemany('INSERT INTO inventory VALUES(?,?,?)', cars)