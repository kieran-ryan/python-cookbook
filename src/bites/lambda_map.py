array = [1, 2, 3]


def increment(x):
    return x + 1


function_map = map(increment, array)
print(list(function_map))
# [2, 3, 4]

lambda_map = map(lambda x: x + 1, array)
print(list(lambda_map))
# [2, 3, 4]
