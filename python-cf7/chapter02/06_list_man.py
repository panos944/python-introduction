fruits = ["Banana", "Orange", "Mango", "Grapes"]

print(f"Initial list: {fruits}")

# Add a fruit at the end of the list
fruits.append("Berry")
print("After adding Berry", fruits)

fruits.append(["Grapes", "Fig"])

print("After adding Grapes, Fig:", fruits)

# insert an element in a specific position
fruits.insert(1, "Coconut")
print("After adding Coconut", fruits)

# Update the first element
fruits[0] = "Melon"
print("After updating the first element:", fruits)

# Update a slice of list (two elements)
fruits[1:3] = ["A", "B", "C"]
print("After slicing:", fruits)

#pop()
removed_item = fruits.pop(2)
print(f"Rmoved item: {removed_item}")
print("After pop():", fruits)

#remove
fruits.remove("C")
print("After remove (C): ", fruits)

idx = fruits.index("A")
print(idx)

item_to_remove = "Grapes"

if item_to_remove in fruits:
    fruits.remove(item_to_remove)
    print(f"{item_to_remove} removed")
else:
    print("insert a valid fruit...")