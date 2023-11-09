
class AllLessons:
    def __init__(self):
        self.lessons = []

    def display(self):
        for lesson in self.lessons:
            lesson.short_info()

    def delete_lesson(self, lesson_unique_index):
        for lesson in self.lessons:
            if lesson.unique_test_number == lesson_unique_index:
                del lesson
                break

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def delete_all_lessons(self):
        self.lessons.clear()