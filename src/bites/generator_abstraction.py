# Order will reflect output e.g. swapping values will result in
# BuzzFizz on common dividends.
_KEYWORD_MAP = {
    3: "Fizz",
    5: "Buzz",
}


def fizzbuzz_matches(number, keyword_map):
    keys = keyword_map.keys()
    for key in keys:
        if number % key == 0:
            yield keyword_map[key]


if __name__ == "__main__":
    matches = set(fizzbuzz_matches(30, _KEYWORD_MAP))
    print("".join(matches))
    # 'FizzBuzz'

    for match in fizzbuzz_matches(30, _KEYWORD_MAP):
        print(match)
    # 'Fizz'
    # 'Buzz'
