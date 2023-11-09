import random
import re
from random import randint

class Helpers:
    @staticmethod
    def password_checker(password_input: str) -> bool:
        """
        Password checker with using regular expression.
        Its check if password contains at least 8 or less than 32 symbols.
        For correct password is need to have len(password) >= 8 and len(password) <= 32;
        Min one lower, one capitalize, one digit and one special symbol from allowed symbol - _ . @
        :param password_input: string password
        :return: bool (True or False)
        """

        if not isinstance(password_input, str):
            raise TypeError("Invalid password type!")
        if not password_input or any(ch.isspace() for ch in password_input) or password_input.isspace():
            raise ValueError("Password can not be white space or contain spaces!")

        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[-_\.@])(?=.*\d).+$'
        if len(password_input) < 8 or len(password_input) > 32:
            print("Your password need to be at least 8 symbols and not more than 32 symbols!")
            return False
        if re.match(pattern, password_input):
            print("This password is strong!")
            return True
        else:
            print("Your password need to contain at least:\nOne digit; One low letter; One capital letter;"
                  " One special symbol from (._-@)")
            return False

    @staticmethod
    def email_validator(email_input: str) -> bool:
        if not isinstance(email_input, str):
            raise TypeError("Email must be a string!")

        if len(email_input) < 6:
            raise ValueError("Email must be a least 6 characters!")

        pattern = r"^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if re.match(pattern, email_input):
            print("Correct E-mail!")
            return True
        return False

    @staticmethod
    def random_ip_generator() -> int:
        return random.randint(1000000000, 100000000000000)

    @staticmethod
    def generate_unique_number(collection_of_numbers):
        while True:
            number = random.randint(1, 1000)
            if number not in collection_of_numbers:
                collection_of_numbers.append(number)
                return number

    @staticmethod
    def positive_number_validator(number):
        if not isinstance(number, int):
            raise TypeError("Student number must to be un integer number!")

        if number <= 0:
            raise ValueError("Student number can not be a negative number or zero!")

    @staticmethod
    def check_instance(obj, class_type):
        if not isinstance(obj, class_type):
            raise TypeError(f"Invalid type! {str(obj).capitalize()} must to be an instance of {class_type} class!")
