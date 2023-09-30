import sqlite3

con = sqlite3.connect("itstep_db.sl3")

cur = con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS students (name TEXT)# ")
#cur.execute("INSERT INTO students (name) values ('Vanya')")
cur. execute("SELECT rowid, name FROM students")
print(cur.fetchall())
con.commit()

con.close()