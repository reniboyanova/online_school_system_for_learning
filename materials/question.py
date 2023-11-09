class Question:
    def __init__(self, title):
        self.title = title
        self._answers = []
        self._correct_answer = 0
        self._question_score = 1

    def display(self):
        print(self.title)
        for index, content in enumerate(self._answers):
            print(f"{chr(65 + index)}) {content}")

    @property
    def question_score(self):
        return self._question_score

    def change_question_score(self, value):
        self._question_score = value

    @property
    def correct_answer(self):
        return self._correct_answer

    def set_correct_answer(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self._answers):
            raise ValueError("Invalid answer index!")
        self._correct_answer = index

    @property
    def answers(self):
        return self._answers

    def add_answer(self, answer):
        if not answer:
            raise ValueError("Answer cannot be empty string!")
        if not isinstance(answer, str):
            raise TypeError("Answer must to be in string format!")
        self.answers.append(answer)

    def increase_score(self, value):
        if value < 0:
            raise ValueError("Score cannot be negative!")
        self.question_score += value

    def decrease_score(self, value):
        if value < 0:
            raise ValueError("Score cannot be negative!")
        self.question_score -= value

    def check_answer(self, selected_index):
        return selected_index == self.correct_answer

    @question_score.setter
    def question_score(self, value):
        self._question_score = value

    @answers.setter
    def answers(self, value):
        self._answers = value


