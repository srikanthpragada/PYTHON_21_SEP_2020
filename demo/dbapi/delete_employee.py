import sqlite3

con = sqlite3.connect(r"c:\classroom\sep21\hr.db")
cur = con.cursor()
id = input("Employee Id :")
cur.execute("delete from employees where id = ?", (id,))
if cur.rowcount == 1:
    print("Deleted Successfully!")
else:
    print("Employee Id not found!")

con.commit()
con.close()
