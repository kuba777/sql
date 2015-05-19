# -*- coding: utf-8 -*-
# Prompt the user whether he or she would like to perform an aggregation (AVG, MAX,
# MIN, or SUM) or exit the program altogether.

import sqlite3

conn = sqlite3.connect("newnum.db")

# create a cursor object to execute SQL commands
cursor = conn.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""
# loop until user enters a valid operation number [1-5]
while True:
    #get user input
    x = raw_input(prompt)

    # if user enters any choice from 1-4
    if x in ["1","2","3","4"]:
        #phrase the corresponding operation text

        operation = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(x)]

        # retrive data

        cursor.execute("SELECT {}(nums) from numbers".format(operation))

        #fetchone() retrives one record from query
        get = cursor.fetchone()

        # output result to screen
        print operation + ": %f" % get[0]

    # if user enters 5
    elif x == "5":
        print "Exit"

        #exit loop
        break






#b = None



#with sqlite3.connect("newnum.db") as connection:
 #   c = connection.cursor()


    # while b != "exit":
    
    #     a = raw_input("Type AVG, MAX, MIN, SUM or Exit: ")
    #     b = a.lower()
        
    #     if b == "avg":
    #         c.execute("SELECT avg(nums) FROM numbers") 
    #     elif b == "max":
    #         c.execute("SELECT max(nums) FROM numbers")
    #     elif b == "min":
    #         c.execute("SELECT min(nums) FROM numbers")
    #     elif b == "sum":
    #         c.execute("SELECT sum(nums) FROM numbers")

    #     elif b == "exit":
    #         break
    #     result = c.fetchone()

    #     print b, result[0]

    

    
