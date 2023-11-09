import datetime

from Python_homework.online_for_teaching_project.project.materials.all_lessons import AllLessons
from Python_homework.online_for_teaching_project.project.materials.all_tests import AllTests
from Python_homework.online_for_teaching_project.project.materials.homework import Homework
from Python_homework.online_for_teaching_project.project.materials.lesson import LessonContent
from Python_homework.online_for_teaching_project.project.materials.task import Task
from Python_homework.online_for_teaching_project.project.materials.test_content import TestContent
from Python_homework.online_for_teaching_project.project.prints.menu_prints import MenuPrints
from Python_homework.online_for_teaching_project.project.users_profile.all_students import AllStudents
from Python_homework.online_for_teaching_project.project.users_profile.register_user import RegisterUser
from Python_homework.online_for_teaching_project.project.utils.utils import Helpers


# from project.materials.lesson import LessonContent
# from project.materials.test_content import TestContent
# from register_user import RegisterUser
# from project.materials.homework import Homework
# from project.materials.task import Task
# from project.users_profile.all_students import AllStudents
# from project.utils.utils import Helpers
# from project.materials.all_tests import AllTests
# from project.materials.all_lessons import AllLessons
# from project.prints.menu_prints import MenuPrints


class Teacher(RegisterUser):
    def __init__(self, speciality):
        super().__init__()
        self.speciality = speciality
        self.students = []
        self.all_lessons_access = AllLessons()
        self.all_test_access = AllTests()

    def view_personal_data(self):
        print(f"First name:           |{self.first_name}    |"
              f"\nLast name:          |{self.last_name}     |"
              f"\nSpeciality:         |{self.speciality}    |"
              f"\nNumber of students: |{len(self.students)} |"
              f"\ne-mail:             |{self.email}         |")

    def short_info(self):
        print(f"Teacher name: {self.first_name} {self.last_name}"
              f"\nSpeciality: {self.speciality}")

    def add_student(self, student_number):
        for student in AllStudents().students:
            if student.student_number == student_number:
                self.students.append(student)
                print(f"Student: {student.first_name} {student.last_name} with student's number: {student.student_number}"
                      f" was add to your students.")
                return
        raise TypeError("Invalid type! Student must to be an instance of Student class!")

    def remove_student(self, student_number):
        for student in self.students:
            if student.student_number == student_number:
                self.students.remove(student)
                return
        print("You don't have a student with this student number!")

    def add_homework_to_student(self, student_number, homework: Homework):
        Helpers.positive_number_validator(student_number)
        Helpers.check_instance(homework, Homework)

        for student in self.students:
            if student.student_number == student_number:
                student.homeworks.append(homework)
                print("You successfully add homework to student!")
                return

    def see_test_results_of_all_students(self):
        for student in self.students:
            print(f"Student: {student.first_name} {student.last_name}")
            for test in student.passed_tests:
                print(f"Test: {test.theme} - {test.total_score_from_test}")

            print("*****************************************************")

    def see_test_result_to_current_student(self, student_number):
        Helpers.positive_number_validator(student_number)

        for student in self.students:
            if student.student_number == student_number:
                print(f"Student: {student.first_name} {student.last_name}")
                for test in student.passed_tests:
                    print(f"Test: {test.theme} - {test.total_score_from_test}")

    def add_task_to_student(self, student_number, task: Task):
        Helpers.positive_number_validator(student_number)
        Helpers.check_instance(task, Task)

        for student in self.students:
            if student.student_number == student_number:
                student.tasks.append(task)
                print("You successfully add task to student!")
                return

    def check_student_homework(self, student_number):
        Helpers.positive_number_validator(student_number)
        for student in self.students:
            if student.student_number == student_number:
                for homework in student.homeworks:
                    if homework.completed:
                        homework.mark_as_well_done()
                    else:
                        print("This homework is not ready yet!")

    def add_to_all_lessons(self, lesson: LessonContent):
        Helpers.check_instance(lesson, LessonContent)
        self.all_lessons_access.add_lesson(lesson)

    def add_to_all_tests(self, test: TestContent):
        Helpers.check_instance(test, TestContent)
        self.all_test_access.add_test(test)

    def person_menu(self):
        print(MenuPrints.TEACHER_MENU_PRINT)

        user_choice = int(input("Make your choice: "))

        Helpers.positive_number_validator(user_choice)
        Helpers.check_instance(user_choice, int)

        if user_choice == 1:
            self.view_personal_data()
        elif user_choice == 2:
            self.change_personal_data()
        elif user_choice == 3:
            print("Please insert a due date: ")
            due_date = datetime.date(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
            homework = Homework(input("Add homework subject:"), input("Add homework description: "), due_date)
            self.add_homework_to_student(int(input("Insert student number, please: ")), homework)
        elif user_choice == 4:
            self.check_student_homework(int(input("Insert student number, please: ")))
        elif user_choice == 5:

            choice = int(input("See all students results - 1, see current student result - 2: "))

            if choice == 1:
                self.see_test_results_of_all_students()
            elif choice == 2:
                self.see_test_result_to_current_student(int(input("Insert student number, please: ")))
            else:
                print("Incorrect choice!")
        elif user_choice == 6:
            task = Task({str(input("Insert first question: ")): '', str(input("Insert second question: ")): '',
                         str(input("Insert third question: ")): ''})
            self.add_task_to_student(int(input("Insert student number, please: ")), task)
        elif user_choice == 7:
            self.add_student(int(input("Insert student number, please: ")))
        elif user_choice == 8:
            choice = input("Are you sure want to remove a student? (y/n) ")
            if choice.lower() == 'y':
                self.remove_student(int(input("Insert student number, please: ")))
                return
        elif user_choice == 9:
            lesson = LessonContent(str(input("Insert lesson theme: ")), str(input("Insert lesson title: ")),
                                   str(input("Insert lesson content: ")))
            self.add_to_all_lessons(lesson)
        elif user_choice == 10:
            test = TestContent(str(input("Insert test theme: ")), int(input("Insert minutes to complete: ")))
            self.add_to_all_tests(test)
        else:
            print("Incorrect choice!")







