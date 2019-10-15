#!/usr/bin/python3

import mysql.connector
conn = mysql.connector.connect(user='test', password='test', database='pytest')
cursor = conn.cursor()
new_employee = ('INSERT INTO employees '
    '(empid, hotdrinks, small, medium, large) '
    'VALUES (%s, %s, %s, %s, %s)')

employee1 = ('1', 'Americano', '2.00', '2.20', '2.40')
employee2 = ('2', 'Latte', '2.20', '2.40', '2.60')
employee3 = ('3', 'Cappuccino', '2.20', '2.40', '2.60')
employee4 = ('4', 'Flat white', '2.20', '2.40', 'null')
employee5 = ('5', 'Chai latte', '2.20', '2.40', '2.60')
employee6 = ('6', 'Dirty Chai Latte', '2.50', '2.70', '2.90')
employee7 = ('7', 'Mocha', '2.50', '2.70', '2.90')
employee8 = ('8', 'Hot Chocolate', '2.40', '2.60', '2.80')
employee9 = ('9', 'Sophie Special', '2.90', '3.10', '3.30')

try:
    cursor.execute(new_employee, employee1)
    cursor.execute(new_employee, employee2)
    cursor.execute(new_employee, employee3)
    cursor.execute(new_employee, employee4)
    cursor.execute(new_employee, employee5)
    cursor.execute(new_employee, employee6)
    cursor.execute(new_employee, employee7)
    cursor.execute(new_employee, employee8)
    cursor.execute(new_employee, employee9)
    conn.commit()
except:
    print('Sorry, there was a problem adding the data')
else:
   print('Data values added!')
cursor.close()
conn.close()