message1 = "Factory"

for i in range(len(message1)):
    print(message1[i] * (i + 1))

for i in range(len(message1)):
    print(message1 * (i + 1), end="*" * (len(message1) -i -1))
    print()