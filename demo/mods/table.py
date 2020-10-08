import sys

if len(sys.argv) < 2:
    print("Usage: python table.py  <number> [size=10]")
    exit(1)  # terminate program with error

num = int(sys.argv[1])
if len(sys.argv) > 2:
    size = int(sys.argv[2])
else:
    size = 10

for i in range(1, size + 1):
    print(f"{num:2} * {i:2} = {i * num:4}")
