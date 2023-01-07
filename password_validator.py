def is_long_enough(password):
    return len(password) >= 8


def has_lowercase(password):
    for i in password:
        if i.islower():
            return True
    return False


def has_uppercase(password):
    for i in password:
        if i.isupper():
            return True
    return False


def has_digit(password):
    for i in password:
        if i.isdigit():
            return True
    return False


def has_special_character(password):
    for i in password:
        if i.isascii():
            return True
    return False