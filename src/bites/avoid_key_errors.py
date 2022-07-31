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


class ContractorAccounts:
    def __init__(self, contractors=None):
        self.contractors = {} if contractors is None else contractors

    def pay_create_assign(self, contractor, amount) -> None:
        """Creates account entry if none existing, then assigns."""
        if contractor not in self.contractors:
            self.contractors[contractor] = 0

        self.contractors[contractor] += amount

    def pay_default_assign(self, contractor, amount):
        """Gets a default if no existing account, then assigns."""
        current_amount = self.contractors.get(contractor, 0)

        self.contractors[contractor] = current_amount + amount

    def pay_assigns(self, contractor, amount):
        """Assigns."""
        self.contractors[contractor] += amount


if __name__ == "__main__":
    db = ContractorAccounts()
    db.pay_create_assign(contractor="Kieran LTD", amount=2000)
    db.pay_create_assign(contractor="Kieran LTD", amount=4500)
    print(db.contractors["Kieran LTD"])  # 6500

    db = ContractorAccounts()
    db.pay_default_assign(contractor="Kieran LTD", amount=2000)
    db.pay_default_assign(contractor="Kieran LTD", amount=4500)
    print(db.contractors["Kieran LTD"])  # 6500

    db = ContractorAccounts(defaultdict(int))  # Default declared as `int` (0)
    db.pay_assigns(contractor="Kieran LTD", amount=2000)
    db.pay_assigns(contractor="Kieran LTD", amount=4500)
    print(db.contractors["Kieran LTD"])  # 6500
