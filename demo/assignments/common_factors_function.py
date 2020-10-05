def common_factors(*numbers, ignore_prime=False):
    min_num = min(numbers)
    factors = []
    for n in range(2, min_num // 2 + 1):
        for num in numbers:
            if num % n != 0:
                break
        else:
            factors.append(n)

    return factors


factors = common_factors(10, 20, 45, 60)
print(factors)

factors = common_factors(15, 45, 255)
print(factors)
