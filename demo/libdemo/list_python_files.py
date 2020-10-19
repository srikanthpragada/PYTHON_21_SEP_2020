import os

files = os.walk(r"c:\classroom\sep21\demo")

for (dirname, dirs, files) in files:
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
