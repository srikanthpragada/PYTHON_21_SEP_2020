
def has_digit(s):
    for c in s:
        if c.isdigit():
            return True
    else:
        return False


def has_upper(s):
    for c in s:
        if c.isupper():
            return True
    else:
        return False