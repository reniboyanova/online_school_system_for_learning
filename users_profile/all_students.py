class AllStudents:
    def __init__(self):
        self.students = []

    def display(self):
        for student in self.students:
            student.short_info()