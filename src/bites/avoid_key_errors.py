"""Avoid `dict` `KeyError`s with `collections.defaultdict`.

With `dict`, assigning to a missing key will throw a `KeyError`. Thus,
when that is not desired, implementations often explicitly apply a
default where the assignment is made.

These implementations can be simplified by using
`collections.defaultdict`; which applies a default at initialisation so
assignments can be made without an existing key.

    * This is cleaner as it abstracts declaration of the default from
      where assignments are made.
    * Err with caution, however. Beyond assignment, trying to access a
      missing key will create one e.g. `print(defaultdict(int)["a"])`
      would add `"a"` to the dictionary and output `0`.
"""
from collections import defaultdict


def pay_create_assign(db: defaultdict | dict, contractor: str, amount: int) -> None:
    """Creates account entry if none exists; assigns otherwise."""
    if contractor not in db:
        db[contractor] = amount
    else:
        db[contractor] += amount


def pay_default_assign(db: defaultdict | dict, contractor: str, amount: int) -> None:
    """Gets a default if no existing account, then assign."""
    current_amount = db.get(contractor, 0)

    db[contractor] = current_amount + amount


def pay_assigns(db: defaultdict, contractor: str, amount: int) -> None:
    """Assign."""
    db[contractor] += amount


if __name__ == "__main__":
    db = {}
    pay_create_assign(db, contractor="Kieran LTD", amount=2000)
    pay_create_assign(db, contractor="Kieran LTD", amount=4500)
    print(db["Kieran LTD"])  # 6500

    db = {}
    pay_default_assign(db, contractor="Kieran LTD", amount=2000)
    pay_default_assign(db, contractor="Kieran LTD", amount=4500)
    print(db["Kieran LTD"])  # 6500

    db = defaultdict(int)
    pay_assigns(db, "Kieran LTD", amount=2000)
    pay_assigns(db, "Kieran LTD", amount=4500)
    print(db["Kieran LTD"])  # 6500
