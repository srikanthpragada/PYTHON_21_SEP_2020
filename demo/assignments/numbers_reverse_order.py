nums = []
while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break

    nums.append(n)

print(sorted(nums, reverse=True))
