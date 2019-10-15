#!/usr/bin/python3

import mysql.connector
conn = mysql.connector.connect(user='test', password='test', database='pytest')
cursor = conn.cursor()

query = ('SELECT empid, hotdrinks, small, medium, large FROM employees')
cursor.execute(query)
for (empid, hotdrinks, small, medium, large) in cursor:
    print(empid, hotdrinks, small, medium, large)
cursor.close()
conn.close()
