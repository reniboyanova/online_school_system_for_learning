# from project.materials.lesson import LessonContent
# from project.materials.question import Question
# from project.materials.test_content import TestContent
# from project.users_profile.student import Student
# from project.users_profile.teacher import Teacher
from Python_homework.online_for_teaching_project.project.materials.lesson import LessonContent
from Python_homework.online_for_teaching_project.project.materials.question import Question
from Python_homework.online_for_teaching_project.project.materials.test_content import TestContent
from Python_homework.online_for_teaching_project.project.users_profile.student import Student
from Python_homework.online_for_teaching_project.project.users_profile.teacher import Teacher


def creating_students(number_of_students):
    students = []
    for _ in range(number_of_students):
        student = Student(int(input("Insert student number: ")))
        student.register_user()
        students.append(student)

    return students


def create_teachers(number_of_teachers):
    teachers = []
    for _ in range(number_of_teachers):
        teacher = Teacher(str(input("Insert teachers speciality: ")))
        teacher.register_user()
        teachers.append(teacher)

    return teachers


def create_sample_tests(number_of_test):
    sample_tests = []

    for _ in range(number_of_test):
        test = TestContent(str(input("Insert test theme: ")), int(input("Insert minutes: ")))
        for i in range(2):
            question = Question(str(input("Question title: ")))
            for j in range(3):
                question.add_answer(str(input("Insert answer: ")))
            question.set_correct_answer(int(input("Insert correct answer as index: ")))
            test.add_question(question)
        sample_tests.append(test)

    return sample_tests


def create_lessons(number_of_lessons):
    lessons = []

    for _ in range(number_of_lessons):
        lesson = LessonContent(str(input("Insert lesson theme: ")),
                               str(input("Insert lesson title: ")), str(input("Insert content: ")))
        lessons.append(lesson)

    return lessons

