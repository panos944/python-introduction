a = range(10)
print(f"Type of a: {type(a)}")

for i in range(1000000):
    if i == 5:
        break
    print(i, end="")
print()

for i in range(10):
    if i == 5:
        continue
    print(i, end="")
print()
print("-" * 10)

for i in range(10):
    if i == 10:
        break
    print(1, end=" | ")
else:
    print("Loop ended normally")

# List of fruits
fruits = ["Banana", "Orange", "Mango", "Grapes"]

fruit_to_check = "Melon"

for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in list")
        break
    else:
        print(f"{fruit_to_check} not in list")

# Happy Hour
print("Why do Python devs never get lost")
print("Becuase they always know where 'in' is!")

if fruit_to_check in fruits:
    print(f"{fruit_to_check} is in list")
else:
    print(f"{fruit_to_check} not in list")

# challenge
print("One line exe")
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} the list")