class Task:
    def __init__(self, task_data: dict):
        self.data = task_data
        self._well_done = False
        self._complete = False
        self._score = 0

    def mark_as_well_done(self):
        self._well_done = True

    def give_task_score(self, value):
        self._score += value

    @property
    def score(self):
        return self._score

    @property
    def well_done(self):
        return self._well_done

    def mark_as_complete(self):
        self._complete = True

