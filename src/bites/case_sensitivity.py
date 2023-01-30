password_old = "s^OV6ß3$i2Ve5"
password_new = "S^Ov6ß3$I2vE5"

print(password_old == password_new)
# False - case sensitive

print(password_old.lower() == password_new.lower())
# True - case insensitive - though fails to convert `ß` to lower case

print(password_old.casefold() == password_new.casefold())
# True - case insensitive
