s = "Welcome"

# List Comprehension
codes = [ord(c) for c in s]
print(codes)

codes = []
for c in s:
    code = ord(c)
    if code not in codes:
        codes.append(code)

print(codes)

