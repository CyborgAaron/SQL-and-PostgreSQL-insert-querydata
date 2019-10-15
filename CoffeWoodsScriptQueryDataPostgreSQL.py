#!/usr/bin/python3

import psycopg2
conn = psycopg2.connect('dbname=coffeetest')
cursor = conn.cursor()
cursor.execute('SELECT empid, hotdrinks, small, medium, large FROM employees')
result = cursor.fetchall()
for data in result:
   print(data[0], data[1], data[2], data[3], data[4], data[5])
cursor.close()
conn.close()