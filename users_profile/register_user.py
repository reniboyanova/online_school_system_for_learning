from abc import ABC, abstractmethod

from Python_homework.online_for_teaching_project.project.materials.test_content import TestContent
from Python_homework.online_for_teaching_project.project.utils.utils import Helpers


# from project.materials.test_content import TestContent
# from project.utils.utils import Helpers


class RegisterUser(ABC):
    def __init__(self):
        """
        Initialize a new RegisterUser object.

        his class represents a user and provides methods for registration, changing personal data,
        and other user-related functionality.

        Attributes:
        _first_name (str): The user's first name.
        _last_name (str): The user's last name.
        _email (str): The user's email address.
        _password (str): The user's password.
        """

        self._first_name = ''
        self._last_name = ''
        self._email = ''
        self._password = ''

    def password_validation(self) -> bool:
        """
        Function will make actual validation of correct user password and set if it's correct.
        Example for correct password: self._password = strongPass12_
        Function use helper method to check if password is correct.
        Input is taking inside the function!
        :return: True or False (bool)
        """

        correct_password = False
        correct_repeat_password = False

        while not correct_password:
            password = input("Please, insert your password: ")
            if Helpers.password_checker(password):
                correct_password = True
                while not correct_repeat_password:
                    repeat_password = input("Please, repeat your password: ")
                    if Helpers.password_checker(repeat_password) and repeat_password == password:
                        self._password = password
                        correct_repeat_password = True
                    if correct_repeat_password and correct_password:
                        break
            if correct_repeat_password and correct_password:
                print(f"{self._first_name} {self._last_name} your password is successfully set!\n")
                return True

    def email_validation(self) -> bool:
        """
        Function will make actual validation of correct user email and set if it's correct.
        Example for correct email: self._email = reni@reni.com
        Function use helper method with regex pattern to check if email is correct.
        Input is taking inside the function!
        :return: True or False (bool)
        """
        correct_email = False
        while not correct_email:
            input_email = input("Please insert your email here: ")
            if Helpers.email_validator(input_email):
                self._email = input_email
                correct_email = True
                break
        return correct_email

    @property
    def email(self):
        """
        Property that return self._email value
        :return: self._email
        """
        return self._email

    def first_name_set(self):
        """
        Function will make actual validation of correct user first name and set if it's correct.
        Example for correct first name: self._first_name = 'Reni'
        Input is taking inside the function!
        """
        first_name = input("Please, insert your first name: ")

        if not isinstance(first_name, str):
            raise TypeError("Incorrect type! First name must to be string!")

        if len(first_name) < 2:
            raise ValueError("First name can not be less than 2 characters!")

        self._first_name = first_name

    @property
    def first_name(self):
        """
        Property that returns value of self._first_name
        :return: self._first_name
        """
        return self._first_name

    @property
    def last_name(self):
        """
        Property that returns value of self._last_name
        :return: self._last_name
        """
        return self._last_name

    def last_name_set(self):
        """
        Function will make actual validation of correct user last name and set if it's correct.
        Example for correct first name: self._last_name = 'Boyanova'
        Input is taking inside the function!
        """
        last_name = input("Please, insert your last name: ")

        if not isinstance(last_name, str):
            raise TypeError("Incorrect type! Last name must to be string!")

        if len(last_name) < 2:
            raise ValueError("Last name can not be less than 2 characters!")

        self._last_name = last_name

    @abstractmethod
    def view_personal_data(self):
        """
        Abstract method for showing personal data, that every derives class will implement as it's needs
        :return:
        """
        pass

    def change_personal_data(self):
        """
        Function that give a permission to change a personal data after input correct password!
        :return:
        """
        password = input("To change your data, please insert your password: ")

        if password == self._password:
            print("Correct password!")
            self.change_personal_data_menu()
        print("Incorrect password!")

    @abstractmethod
    def short_info(self):
        """
        Abstract method that implements a
        :return:
        """
        pass

    def change_personal_data_menu(self):
        print(f"You are with {self.__class__.__name__.upper()} profile! You can change only your e-mail and password!")
        print("To change e-mail press - 1 | To change password press - 2")

        user_choice = int(input())

        if user_choice == 1:
            new_email = input("New email: ")
            self.change_email(new_email)
        elif user_choice == 2:
            new_password = input("New password: ")
            self.change_password(new_password)
        else:
            print("Invalid user choice!")

    def register_user(self):
        self.first_name_set()
        self.last_name_set()
        self.email_validation()
        self.password_validation()

    def change_password(self, value):
        if Helpers.password_checker(value):
            repeat_password = input("Repeat password to confirm changing: ")

            if Helpers.password_checker(repeat_password):
                self._password = value
                return self._password

            raise ValueError("Repeating password is not same!")
        raise ValueError("Password is not correct! Please provide correct password!")

    def change_email(self, value):
        if Helpers.email_validator(value):
            self._email = value

    @abstractmethod
    def person_menu(self):
        pass

    @staticmethod
    def complete_sample_test(tests: list):
        for test in tests:
            Helpers.check_instance(test, TestContent)
            test.start_test()
