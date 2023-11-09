import datetime


class Homework:
    def __init__(self, subject, description, due_date):
        self.subject = subject
        self.description = description
        self.due_date = due_date
        self.data = ''
        self._completed = False
        self._submission_date = None
        self._well_done = False
        self._score = 0

    def mark_as_completed(self, data_value):
        if not self._completed:
            current_date = datetime.date.today()
            if current_date <= self.due_date:
                self._completed = True
                self._submission_date = current_date
                self.data = data_value
            else:
                print("Attention! Due date for this homework is passed!")

    def mark_as_uncompleted(self):
        if self._completed:
            self.data = ''
            self.description = ''
            self._completed = False
            self._submission_date = None
            return
        print("It is not completed yet!")

    def __str__(self):
        status = "COMPLETED" if self._completed else "UNCOMPLETED"
        submission_date = self._submission_date.strftime("%d/%m/%Y") if self._submission_date else "N/A"
        return (f"SUBJECT: {self.subject}"
                f"\nDUE DATE: {self.due_date}"
                f"\nSTATUS: {status}"
                f"\nSUBMISSION DATE: {submission_date}")

    @property
    def completed(self):
        return self._completed

    @property
    def submission_date(self):
        return self._submission_date

    def short_info(self):
        print(f"SUBJECT: {self.subject}"
              f"\nDESCRIPTION: {self.description}"
              f"\nDUE DATE: {self.due_date}"
              f"\nSTATUS: {self.completed}")

    def mark_as_well_done(self):
        self._well_done = True

    def give_homework_score(self, value):
        self._score += value

    @property
    def score(self):
        return self._score

    @property
    def well_done(self):
        return self._well_done




