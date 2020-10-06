def extract_digits(s):
    digits = []
    for c in s:
        if c.isdigit():
            digits.append(c)

    return "".join(digits)


def contains_digit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


values = ['Abc223', '345xyz555', 'pqr', '48484']

# Extract digits from each string
for v in map(extract_digits, values):
    print(v)

# Show strings that contain digits
for v in filter(contains_digit, values):
    print(v)
