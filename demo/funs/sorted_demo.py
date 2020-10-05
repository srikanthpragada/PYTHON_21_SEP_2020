def odd_even(n):
    return 1 if n % 2 == 0 else 0


scores = [60, 45, -30, 67, 88, 34, -90]
#
# for n in sorted(scores, key=abs):
#     print(n)

for n in sorted(scores, key=odd_even):
    print(n)
