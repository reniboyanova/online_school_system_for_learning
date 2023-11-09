# from project.materials.all_lessons import AllLessons
# from project.materials.all_tests import AllTests
# from project.users_profile.all_students import AllStudents
# from creating import creating_students, create_teachers, create_sample_tests, create_lessons
# from project.users_profile.all_teachers import AllTeachers
# from project.users_profile.anonymous_user import AnonymousUser
# from project.users_profile.student import Student
# from project.users_profile.teacher import Teacher
from Python_homework.online_for_teaching_project.project.materials.all_lessons import AllLessons
from Python_homework.online_for_teaching_project.project.materials.all_tests import AllTests
from Python_homework.online_for_teaching_project.project.simulation.creating import creating_students, create_teachers, \
    create_sample_tests, create_lessons
from Python_homework.online_for_teaching_project.project.users_profile.all_students import AllStudents
from Python_homework.online_for_teaching_project.project.users_profile.all_teachers import AllTeachers
from Python_homework.online_for_teaching_project.project.users_profile.anonymous_user import AnonymousUser
from Python_homework.online_for_teaching_project.project.users_profile.student import Student
from Python_homework.online_for_teaching_project.project.users_profile.teacher import Teacher


class Simulation:
    def __init__(self):
        self.students = AllStudents()
        self.teachers = AllTeachers()
        self.tests = AllTests()
        self.lessons = AllLessons()

    def simulation_with_creation(self):
        self.students.students = creating_students(int(input("Insert number of students that you want to create: ")))
        self.teachers.teachers = create_teachers(int(input("Insert number of teachers that you want to create: ")))
        self.tests.tests = create_sample_tests(int(input("Insert number of tests that you want to create: ")))
        self.lessons.lessons = create_lessons(int(input("Insert number of lessons that you want to create: ")))

    def anonymous_user_simulation(self):
        anon_user = AnonymousUser()
        anon_user.view_content()
        anon_user.see_lessons(self.lessons.lessons)
        anon_user.complete_sample_test(self.tests.tests)

    @staticmethod
    def single_teacher_simulation():
        teacher_reni = Teacher("arts")
        teacher_reni.register_user()
        teacher_reni.person_menu()

    @staticmethod
    def single_student_simulation():
        student_bobi = Student(int(input("Insert a student number: ")))
        student_bobi.register_user()
        student_bobi.short_info()
        student_bobi.person_menu()

    def add_lessons_to_all_lessons(self):
        self.lessons.lessons = create_lessons(int(input("Insert number of lessons that you want to create: ")))

    def add_test_to_all_tests(self):
        self.tests.tests = create_sample_tests(int(input("Insert number of tests that you want to create: ")))


if __name__ == '__main__':
    simulation_project = Simulation()
    simulation_project.simulation_with_creation()
