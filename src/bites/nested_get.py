from functools import reduce
from operator import getitem


def nested_get(dict_, keys):
    return reduce(getitem, keys, dict_)


if __name__ == "__main__":
    nested_dict = {"school": {"students": {"name": "Kieran"}}}
    keys = ("school", "students", "name")
    print(nested_get(nested_dict, keys))
    # 'Kieran'
