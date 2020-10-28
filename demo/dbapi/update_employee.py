import sqlite3

con = sqlite3.connect(r"c:\classroom\sep21\hr.db")
cur = con.cursor()
id = input("Id :")
salary = input("Salary : ")
try:
    cur.execute("update employees set salary = ? where id = ?", (salary,id))
    if cur.rowcount == 1:
        print("Updated Successfully!")
        con.commit()
    else:
        print("Employee id is not found!")
except Exception as ex:
    print("Sorry! Could not update employee due to error!")


con.close()
