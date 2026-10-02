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
    print(f"{a} + {b} = " + add(a,b))
    print(f"{a} - {b}= " + subtract(a,b))
    print(f"{a} * {b} = " + multiply(a,b))
    print(f"{a} / {b} = " + divide(a,b))
    print(f"{a}^{b} = " + pow(a,b))
    print(f"abs({a})  = " + abs(a))
    print(f"mod({a},{b}) = " + mod(a,b))