a = 10
b = 0
try:
    c = a / b
    print(c)
except ValueError as ex:
    print("Error :", ex)
except KeyError:
    print("Key Error")
else:
    print("Job Done!")
finally:
    print("Finally!")

print("All over!")
