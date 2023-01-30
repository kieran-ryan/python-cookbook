from contextlib import contextmanager, suppress


@contextmanager
def ignore(*exceptions):
    try:
        yield
    except exceptions:
        pass


def _raise_exception():
    raise TypeError


if __name__ == "__main__":
    with ignore(ValueError, TypeError):
        _raise_exception()
    print("Exception was ignored")  # 'Exception was ignored'

    with suppress(ValueError, TypeError):
        _raise_exception()
    print("Exception was ignored")  # 'Exception was ignored'
