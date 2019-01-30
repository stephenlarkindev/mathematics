def AND(x, y):
    return bool(x * y)


def OR(x, y):
    return bool(1 - (1 - x)*(1 - y))


def NOT(x):
    return bool(1 - x)


print(AND(1, 1))  # True
print(OR(1, 1))  # True
print(OR(1, 0))  # True
print(OR(0, 1))  # True
print(NOT(0))  # True

print()

print(AND(1, 0))  # False
print(OR(0, 0))  # False
print(NOT(1))  # False
