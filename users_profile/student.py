import time

from Python_homework.online_for_teaching_project.project.materials.all_tests import AllTests
from Python_homework.online_for_teaching_project.project.materials.test_content import TestContent
from Python_homework.online_for_teaching_project.project.prints.menu_prints import MenuPrints
from Python_homework.online_for_teaching_project.project.users_profile.register_user import RegisterUser
from Python_homework.online_for_teaching_project.project.utils.utils import Helpers


class Student(RegisterUser):
    def __init__(self, student_number):
        super().__init__()
        self.student_number = student_number
        self.personal_score = 0
        self.passed_tests = []
        self.homeworks = []
        self.tasks = []

    def view_personal_data(self):
        print(f"First name:      |{self.first_name}    |"
              f"\nLast name:     |{self.last_name}     |"
              f"\nStudent number:|{self.student_number}|"
              f"\nScore:         |{self.personal_score}|"
              f"\ne-mail:        |{self.email}         |")

    def short_info(self):
        print(f"Student name: {self.first_name} {self.last_name}"
              f"\nStudent number: {self.student_number}"
              f"\nStudent score: {self.personal_score}")

    def complete_test(self, available_tests):
        while True:
            print("Available tests:")
            for index, test in enumerate(available_tests, start=1):
                print(f"{index}. {test.test_name}")

            try:
                choice = int(input("Choose a test (enter the number): "))
                if 1 <= choice <= len(available_tests):
                    chosen_test = available_tests[choice - 1]
                    Helpers.check_instance(chosen_test, TestContent)
                    chosen_test.start_test()
                    self.personal_score += chosen_test.total_score_from_test
                    self.passed_tests.append(chosen_test)
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_all_tests(self):
        for test in self.passed_tests:
            test.info()

    def upload_homework(self):
        for hw in self.homeworks:
            if not hw.completed:
                print(hw.short_info())

                data_for_homework = input("Please upload your solution: ")
                hw.mark_as_completed(data_for_homework)

                time.sleep(1)
                print("█▒▒▒▒▒▒▒▒▒ 10%")
                time.sleep(2)
                print("██████▒▒▒▒ 60%")
                time.sleep(3)
                print("██████████ 100%")

            make_another_hw = input("\nDo you want to make another homework? (y/n) ")
            if not make_another_hw.lower() == 'y':
                break

    def complete_task(self):
        for task in self.tasks:
            if not task.completed:
                for questions, answers in task.task_data.items():
                    if not questions:
                        print(f"Please provide an answer of question:\n{questions}:\n")
                        answ = input("Answer: ")
                        time.sleep(1)
                        print("████▒▒▒▒▒▒ 40%")
                        time.sleep(2)
                        print("██████████ 100%")
                        task.task_data[questions] = answ

            task.mark_as_complete()

            make_another_task = input("\nDo you want to make another task? (y/n) ")
            if not make_another_task.lower() == 'y':
                break

    def person_menu(self):
        print(MenuPrints.PERSONAL_MENU_PRINT)

        user_choice = int(input("Make your choice: "))

        Helpers.positive_number_validator(user_choice)
        Helpers.check_instance(user_choice, int)

        if user_choice == 1:
            self.view_personal_data()
        elif user_choice == 2:
            self.change_personal_data()
        elif user_choice == 3:
            self.upload_homework()
        elif user_choice == 4:
            self.complete_task()
        elif user_choice == 5:
            self.complete_test(AllTests().tests)
        else:
            print("Incorrect choice!")


if __name__ == '__main__':
    student_reni = Student(int(input("Insert student number: ")))
    student_reni.register_user()
