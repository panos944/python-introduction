import math

name = "Alice"
age="20"

print("CF7")
print("PI:", math.pi)

print(name, "is", age, "years old")

print("-----String Concatenetation------")
# print(name = "is" + age + "years old")

print(name + "is" + str(age) + "years old")


#Python 2 style

print()
print("Python2 style")
print("PI = %6.2f" %math.pi)
print("%s is %s years old" %(name, age))

print("Age is {0:2s}".format(age))

print("PI = {0:.3f} and age = {1}".format(math.pi, age))

print("{0} is {1} years old{2}".format(name, age, "**"))
print("{0} is {1} years old".format(name, age), end="**")

#f-strings
print(f"{name} is {age} years old")