def wish(name, message="Hello"):
    print(f"{message}, {name}")


def fill(lst, size=None):
    if size is None:
        size = len(lst)


wish("Jack", "Hi")
wish("Steve")
wish(message='Good Morning', name="Bill")
wish(name="Larry")
# wish(message='Hi')
