class AllTeachers:
    def __init__(self):
        self.teachers = []

    def display(self):
        for teacher in self.teachers:
            teacher.short_info()