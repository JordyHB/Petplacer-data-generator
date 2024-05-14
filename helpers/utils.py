import random
import string


def load_file_into_mem(path):
    with open(path) as f:
        return f.read().split()


def gen_dummy_phone_number():
    # Makes a list with 8 random digits
    random_digits = [random.randint(1, 9) for _ in range(8)]
    # Convert each random digit to a string and join them into a single string
    random_digit_string = "".join(str(digit) for digit in random_digits)
    return f"06{random_digit_string}"


def gen_dummy_email(name):
    possible_suffixes = ["gmail.com", "outlook.com", "hotmail.nl", "yahoo.com"]
    # Concat an email looking string using the name and 1 of the possible suffixes
    return f"{name}@{random.choice(possible_suffixes)}"


def gen_dummy_postalcode():
    # creates random number
    number_part = str(random.randint(1000, 9999))
    # Creates 2 random Letters and joins them into a string
    letter_part = "".join(random.choice(string.ascii_uppercase) for _ in range(2))
    return f"{number_part} {letter_part}"
