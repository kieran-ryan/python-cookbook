import functools


def multiply(x, y):
    return x * y


multiply_by_three = functools.partial(multiply, y=3)

print(multiply_by_three(6))
# 18
