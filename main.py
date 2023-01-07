import password_validator

# Prompt the user to enter a password
password = input("Enter a password: ")

# Check the password against the good password rules
if password_validator.is_long_enough(password) and password_validator.has_lowercase(password) and password_validator.has_uppercase(password) and password_validator.has_digit(password) and password_validator.has_special_character(password):
    print("Your password is strong.")
else:
    print("Your password is weak. Please try again.")
