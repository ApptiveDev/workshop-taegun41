import random
def add(a, b):
    return a+b


def subtract(a, b):
    return a - b



def multiply(a, b):
    pass


def divide(a, b):
    pass


def pow(a, b):
    return a ** b


def abs(a):
    return abs(a)


def mod(a, b):
    return a % b


if __name__ == "__main__":
    a = random.random()
    b = random.random()
    print("a + b = " + add(a,b))
    print("a - b = " + subtract(a,b))
    print("a * b = " + multiply(a,b))
    print("a / b = " + divide(a,b))
    print("a^b = " + pow(a,b))
    print("abs(a)  = " + abs(a))
    print("mod(a,b) = " + mod(a,b))
    pass

