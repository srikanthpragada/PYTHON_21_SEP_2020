# Print whether a number is prime or not

num = int(input("Enter number :"))
for i in range(2, num // 2 + 1):
    if num % i == 0:
         print('Not a prime number')
         break
else:
    print("Prime number")

print('The End')