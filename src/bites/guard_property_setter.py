class Employee:

    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise ValueError("Email must be a string")
        self._email = value


if __name__ == "__main__":
    employee = Employee(email=5)  # Raises `ValueError`
