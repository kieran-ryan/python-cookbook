password_old = "s^OV6ß3$i2Ve5"
password_new = "S^Ov6ss3$I2vE5"

print(password_old == password_new)
# False - not exact match

print(password_old.lower() == password_new.lower())
# False - `ß` not converted to its lower case (`ss`)

print(password_old.casefold() == password_new.casefold())
# True - case insensitive match
# New password is lowercase of previous and should be rejected
