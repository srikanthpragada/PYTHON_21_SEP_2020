names = ['Python', 'Java', 'C#','C']
ages = [29, 25, 20]

# for idx, name in enumerate(names):
#     print(name, ages[idx])

for name, age in zip(names, ages):
    print(name, age)
