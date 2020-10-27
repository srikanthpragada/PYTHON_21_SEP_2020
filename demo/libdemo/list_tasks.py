from datetime import datetime, timedelta

f = open("tasks.txt", "rt")

tasks = {}

for line in f:
    parts = line.strip().split(",")  # Remove trailing whitespace and then split
    if len(parts) < 2:
        continue

    try:
        stdate = datetime.strptime(parts[1], '%d-%m-%Y')
        if len(parts) > 2:
            enddate = datetime.strptime(parts[2], '%d-%m-%Y')
        else:
            enddate = datetime.today()

        days = (enddate - stdate).days
        tasks[parts[0]] = days  # add to dict
    except Exception as ex:
        print('Error line :', line)
        continue

for task, days in sorted(tasks.items(), key=lambda t: t[1]):
    print(f"{task:30} {days:3}")
