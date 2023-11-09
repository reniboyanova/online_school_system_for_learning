# from users_profile.administrator import Administrator
# from users_profile.student import Student
# from users_profile.teacher import Teacher
# from
from Python_homework.online_for_teaching_project.project.users_profile.administrator import Administrator
from Python_homework.online_for_teaching_project.project.users_profile.student import Student
from Python_homework.online_for_teaching_project.project.users_profile.teacher import Teacher


class HomePageContent:
    def __init__(self):
        self.last_news = []
        self.last_added_lessons = []
        self.last_added_tests = []
        self.our_best_score_students = []
        self.our_teachers = []

    def lest_news_display(self):
        print("*********** LAST NEWS ***********")
        for news in self.last_news:
            news.short_info()

    def lest_lessons_display(self):
        print("*********** LAST LESSONS ***********")
        for lesson in self.last_added_lessons:
            lesson.short_info()

    def our_best_students(self):
        sorted_students = sorted(self.our_best_score_students, key=lambda student: student.personal_score, reverse=True)
        top_3_students = sorted_students[:3]
        print("*********** BEST STUDENTS ***********")
        for student_ in top_3_students:
            student_.short_info()

    def our_teachers(self):
        print("*********** OUR TEACHERS ***********")
        for teacher in self.our_teachers:
            teacher.short_info()

    def register(self, odj):
        if isinstance(odj, Student) or isinstance(odj, Teacher) or isinstance(obj, Administrator):
            return
        print("*********** REGISTRATION ***********")
        new_student_registration = Student(int(input("Insert student number: ")))
        del obj
        return new_student_registration

    def display(self):
        pass