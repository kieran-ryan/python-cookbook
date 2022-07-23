import functools


def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions)


def add_two(n):
    return n + 2


def multiply_by_three(n):
    return n * 3


if __name__ == "__main__":
    my_func = compose(add_two, multiply_by_three)
    print(my_func(2))
    # 12
