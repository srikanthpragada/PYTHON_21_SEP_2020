import sqlite3

file = open("data.txt", "rt")
con = sqlite3.connect(r"c:\classroom\sep21\hr.db")
cur = con.cursor()

for line in file.readlines():
    parts = line.split(",")
    if len(parts) < 3:
        continue

    values = [v.strip() for v in parts]  # Strip spaces from each value
    try:
        cur.execute("insert into employees(fullname,job,salary) values(?,?,?)", values)
        print(f"{values[0]} inserted successfully!")
    except:
        pass

con.commit()
con.close()
