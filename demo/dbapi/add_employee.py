import sqlite3

con = sqlite3.connect(r"c:\classroom\sep21\hr.db")
cur = con.cursor()
fullname = input("Fullname    :")
job = input("Job :")
salary = input("Salary : ")

cur.execute("insert into employees(fullname, job, salary) values(?,?,?)",
                                  (fullname, job, salary))
print(f"Inserted {cur.rowcount} row(s)")
con.commit()
con.close()
