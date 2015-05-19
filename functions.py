# -*- coding: utf-8 -*-
# SQLite functions

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # create a dictionary of sql queries
    sql = {'average': "SELECT avg(population) FROM population",
        'maximum' : "SELECT max(population) FROM population",
        'minimum' : "SELECT min(population) FROM population", 
        'sum' : "SELECT sum(population) FROM population",
        'count': "SELECT count(city) FROM population"}

    # run each sql query item in the dictionary - iteritems returns (key, value)
    for keys, values in sql.iteritems(): 

        #run sql
        c.execute(values)

        # fetchone() retrievies one record from the query
        results = c.fetchone()

        # output the results to screen
        print keys + ":", results[0]

