from Python_homework.online_for_teaching_project.project.prints import menu_prints
from all_lessons import AllLessons
from all_tests import AllTests
from home_page import HomePageContent


class Menu:
    def __init__(self):
        self.home_content = HomePageContent()
        self.all_lessons = AllLessons()
        self.all_tests = AllTests()

    def see_menu(self):
        print(menu_prints.MenuPrints.START_MENU_PRINT)

        user_choice = int(input("---> "))

        if user_choice == 1:
            self.home_content.display()

        elif user_choice == 2:
            self.all_lessons.display()
