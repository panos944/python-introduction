bag = {"eggs", "oranges", "bananas"}
print("Initial bag:", bag)

#Add a new item
bag.add("bananas")
print("Bag after adding bananas", bag)

# #Remove
# bag.remove("bananas")
# print("Bag after removing bananas: ", bag)

for item in bag:
    print(item, end="")
print()