from functools import reduce


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles...")
        func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add budge")
        func(*args, **kwargs)

    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")


# get_ice_cream("Vanila")

def repeat(n):
    def deco(fn):
        def wrapper(*args, **kwargs):
            res = None
            for _ in range(n):
                res = fn(*args, **kwargs)
            return res

        return wrapper

    return deco


@repeat(3)
def say(msg):
    print(msg)


# say('Hello World!')
def product(lst):
    return lambda a, b: a + b, lst


print(product([1, 2, 3, 4]))

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

list3 = list(map(lambda x, y: x + y, list1, list2))
print(list3)