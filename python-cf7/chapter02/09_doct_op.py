#populate dict
products = {
    1:"apple",
    2:"banana",
    3:"honey",
    4:"melon"
}

print(f"Initial dict: {products}")

#Insert a new key: value pair
products[3] = "orange"
print(f"Dict after insertion: {products}")

product_10 = products.get(10)
print(product_10)

del products[1]
print(f"After deleting key 1 {products}")

removed_item = products.pop(3)
print(f"removed item: {removed_item}")
print(f"After removal: {products}")

# Delete: remove the "last" inserted item
key, value = products.popitem()
print(f"Key:{key}, Value:{value}")

print(products)

key_to_check = 20

if key_to_check in products:
    print(f"key: {key_to_check}")
else:
    print(f"Key {key_to_check} does not exist")

#iterate
for key in products:
    print(key, ":", products[key])

print("------------")
for key in products.keys:
    print(key, ":", products[key])

print("------------")
for value in products.values():
    print(value, ":", products[key])

print("------------")
for key,value in products.items():
    print(value, ":", products[key])