import sqlite3
con=sqlite3.connect('database3.db')
print('opened database successfully')
con.execute('CREATE TABLE book(name char(20),author char(20),pdf char(20));')
print('table created successfully')
con.close()