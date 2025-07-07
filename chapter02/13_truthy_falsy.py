# Falsy - Truthy Value
# Falsy: 0, 0.0, 0j, "", [], ()

empty_dict = {}
print(type(empty_dict))

a = 5

if a > 0 and a < 10:
    print("Valiud number")

if 0 < a < 10:
    print("Valid number")

