import sqlite3

try:
    con = sqlite3.connect(r"c:\classroom\sep21\hr.db")
except Exception as ex:
    print("Could not connect to database! Error :", ex)
    exit(1)   # Terminate with error

try:
    cur = con.cursor()
    cur.execute("select sum(salary), avg(salary) from employees")
    totals = cur.fetchone()
    print(f"Total   Salary :  {totals[0]:.0f}")
    print(f"Average Salary :  {totals[1]:.0f}")
except Exception as ex:
    print(ex)
finally:
    con.close()