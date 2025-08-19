from functools import reduce


def calculate(operation, *args):
    if operation == 'add':
        return sum(args)
    elif operation == "multiply":
        return reduce(lambda x, y: x * y, args)
    elif operation == "max":
        return max(args)
    elif operation == "min":
        return min(args)
    else:
        return "Invalid operation"


print(calculate("multiply", 1, 2, 3))
print(calculate("add", 1, 2, 3))
print(calculate("min", 1, 2, 3))
print(calculate("max", 1, 2, 3))
print(calculate("abc", 1, 2, 3))
