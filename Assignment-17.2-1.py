xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# 1
for item in xs:
    print(item)

# 2
for index, number in enumerate(xs):
    print("Number: " + str(number) + ". Its square: " + str(number**2))

# 3
total = 0
for item in xs:
    total += item
print(total)

# 4
product = 1
for item in xs:
    product *= item
print(product)
