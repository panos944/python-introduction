items = [1, 2, 3.14, True, "Hello CF"]

for item in items:
    print(item, end=" ")
print()

nest_list = [
    [1, 2],
    [3, 4],
    [5, 6]
]

#nest-list = [[1, 2], [3, 4],[5, 6]]

print(f"first list item: {nest_list[0]}")

#[3, 4]
print(nest_list[1], nest_list[0], sep=", ")

# slicing ???
