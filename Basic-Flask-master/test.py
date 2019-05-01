import sqlite3 as sql

conn = sql.connect("data.db")

c = conn.cursor()
# c.execute("drop table formdata")
c.execute("CREATE TABLE \
formdata(id INTEGER PRIMARY KEY, email varchar(100), name varchar(1000), mob varchar(1000),\
 role varchar(1000), cmnt varchar(1000))")

conn.commit()
conn.close()
