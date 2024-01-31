import sqlite3

conn = sqlite3.connect("database.db")

print("opened database successfully")

query = "CREATE TABLE IF NOT EXISTS donor (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,gender TEXT,email TEXT,bloodGroup TEXT,province TEXT,city TEXT,phone TEXT,country TEXT,organ TEXT,cause TEXT,hasDonated BOOLEAN DEFAULT 0)"
conn.execute(query)

query2 = "CREATE TABLE IF NOT EXISTS requesters (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,gender TEXT,email TEXT,bloodGroup TEXT,province TEXT,city TEXT,phone TEXT,country TEXT,organ_required TEXT,cause TEXT, donorId INTEGER DEFAULT NULL)"
conn.execute(query2)


print('table created successfully')

conn.close()