def wish(*names, message='Hello'):
    print(type(names))
    for n in names:
        print(f"{message}, {n}")


wish('Larry', 'Mike')
wish('Larry', 'Mike', message="Hi")
