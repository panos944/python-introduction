# Define a tuple of studets
students = ["Alice", "Bob", "Charlie"]

print(f"{students}: {type(students)}")

#iteration
for index, student in enumerate(students):
    print(f"{index}: {student}")

for students in students:
    print(student)

first_st, second_st, third_st = students[0],students[1],students[2]

print(f"first_st: {first_st}")
print(f"first_st: {second_st}")
print(f"first_st: {third_st}")

student = list(students)
students[0] = "Helen"
students = tuple(students)

print(f"{students}, {type(students)}")