import sqlite3
con=sqlite3.connect('data3.db')
print("success")
con.execute('CREATE TABLE student(Name TEXT, physics TEXT,chemistry TEXT);')
print("table successful")
con.close()