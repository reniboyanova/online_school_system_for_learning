# from project.utils.utils import Helpers
# from project.materials import home_page
# from project.materials.test_content import TestContent
from Python_homework.online_for_teaching_project.project.materials import home_page
from Python_homework.online_for_teaching_project.project.materials.test_content import TestContent
from Python_homework.online_for_teaching_project.project.users_profile.student import Student
from Python_homework.online_for_teaching_project.project.utils.utils import Helpers

ip_random_generator = Helpers.random_ip_generator()


class AnonymousUser:
    def __init__(self):
        self._information = f"{self.__class__.__name__} with IP address: {ip_random_generator}"

    @staticmethod
    def view_content():
        home_page.HomePageContent().display()

    @staticmethod
    def complete_sample_test(tests: list):
        for test in tests:
            Helpers.check_instance(test, TestContent)
            test.start_test()

    @staticmethod
    def see_lessons(lessons: list):
        for lesson in lessons:
            lesson.short_info()

    def registration(self):
        obj = Student(int(input("Insert student number: ")))
        obj.register_user()
        return obj




