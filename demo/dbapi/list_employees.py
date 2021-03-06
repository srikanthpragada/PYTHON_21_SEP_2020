import sqlite3

try:
    con = sqlite3.connect(r"c:\classroom\sep21\hr.db")
except Exception as ex:
    print("Could not connect to database! Error :", ex)
    exit(1)   # Terminate with error

try:
    cur = con.cursor()
    cur.execute("select * from employees")
    for emp in cur.fetchall():
        print(f"{emp[0]:5} {emp[1]:30}  {emp[2]:10} {emp[3]:10}")
except Exception as ex:
    print(ex)
finally:
    con.close()