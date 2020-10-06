def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


nums = [20, 23, 66, 73]

for n in filter(isprime, nums):
    print(n)
