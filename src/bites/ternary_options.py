is_green = True

first_ternary = ("Fail", "Pass")[is_green]
second_ternary = is_green and "Pass" or "Fail"
third_ternary = "Pass" if is_green else "Fail"

"""
`first_ternary` is almost twice as slow as the listed alternatives.
However, if acting on an existing tuple variable, it can be as fast or
faster and require less code, compared to performing tuple unpacking or
indexing to use the alternatives.

`second_ternary` and `third ternary` have a negligible difference in
performance. However, `third_ternary` has arguably the best
readability.

Recommendations:
    * Use `first_ternary` for existing tuples.
    * Use `third_ternary` in general.
"""


if __name__ == "__main__":
    print(first_ternary)  # 'Pass'
    print(second_ternary)  # 'Pass'
    print(third_ternary)  # 'Pass'
