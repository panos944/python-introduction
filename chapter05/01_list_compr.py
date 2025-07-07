list_of_ints = [1, 2, 3, 4, 5, 6, 7]

#1. squared nums using list compr
sq_nums_compr = [num ** 2 for num in list_of_ints]
print(sq_nums_compr)

#2. squared unms using map function
sq_nums_map = list(map(lambda num: num ** 2, list_of_ints))
print(sq_nums_map)

#3. squared nums using a function
def square_function(num):
    return num ** 2

sq_nums_func = [square_function(num) for num in list_of_ints]

#4. use  "square function" and map
sq_nums_func = list(map(square_function, list_of_ints))

# filter and square only with list compr

filtered_sq_list_compr = [num ** 2 for num in list_of_ints if num < 5]