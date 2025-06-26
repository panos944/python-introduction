ages = [19, 23, 25, 35, 65]

print("Initial list of ages:", ages)

for age in ages:
    print(age, end=", ")
print()

for index, value in enumerate(ages):
    print(f"Index: {index}, Value:{value}")

