import time

from Python_homework.online_for_teaching_project.project.materials.question import Question
from Python_homework.online_for_teaching_project.project.utils.utils import Helpers

math_test_easy = '../files/questions.txt'
unique_test_numbers = []
unique_num = Helpers.generate_unique_number(unique_test_numbers)


class TestContent:
    def __init__(self, theme, time_to_complete):
        self.theme = theme
        self.time_to_complete = time_to_complete
        self._questions = []
        self._total_score_from_test = 0
        self._test_duration = None
        self._unique_test_number = unique_num

    @property
    def number_of_questions(self):
        return len(self._questions)

    def start_test(self):
        print(f"Test THEME is: {self.theme}\nNUMBER OF QUESTIONS: {self.number_of_questions}"
              f"\nTIME TO COMPLETE: {self.time_to_complete:02}:00 minutes!")

        print("Lets start! Loading....\n███▒▒▒▒▒▒▒ 30%")
        time.sleep(2)
        print("███████▒▒▒ 70%")
        time.sleep(1)
        print("██████████ 100%")

        start_time = time.time()

        for question in self._questions:
            question.display()
            time.sleep(1)

            user_answer = int(input("\nPlease insert your answer: "))

            # to try it with try catch block?
            if not isinstance(user_answer, int):
                raise TypeError("Your choice need to be integer number from 0 - 999 ")

            if user_answer == question.correct_answer:
                time.sleep(1)
                print("Correct answer!")
                self._total_score_from_test += question.question_score

            else:
                time.sleep(1)
                print("Incorrect answer!")

        end_time = time.time()

        self._test_duration = (end_time - start_time) / 60

    @property
    def test_duration(self):
        return self._test_duration

    @property
    def total_score_from_test(self):
        return self._total_score_from_test

    def info(self):
        if self.test_duration < 1:
            duration_text = f"YOUR TIME DURATION TO COMPLETE WAS: {self.test_duration * 60:.0f} seconds!"
        else:
            minutes = int(self.test_duration)
            seconds = int((self.test_duration - minutes) * 60)
            duration_text = f"YOUR TIME DURATION TO COMPLETE WAS: {minutes:02}:{seconds:.0f} minutes!"

        print(f"Test THEME is: {self.theme}"
              f"\nNUMBER OF QUESTIONS: {self.number_of_questions}"
              f"\nTOTAL SCORE: {self.total_score_from_test}"
              f"\n{duration_text}")

    def add_question(self, question: Question):
        if not isinstance(question, Question):
            raise TypeError("Question must be an instance of the Question class")

        self._questions.append(question)

    def read_questions_from_file_and_save_it(self):
        with open(math_test_easy, "r") as file:
            lines = file.readlines()

        for i in range(0, len(lines), 5):
            question_text = lines[i].strip()
            answers = [lines[i + 1].strip(), lines[i + 2].strip(), lines[i + 3].strip()]
            correct_answer_index = int(lines[i + 4].strip())

            question = Question(question_text)
            question.answers = answers

            question.set_correct_answer(correct_answer_index)

            self.add_question(question)

        file.close()

    def short_info(self):
        print(f"Test THEME is: {self.theme}"
              f"\nNUMBER OF QUESTIONS: {self.number_of_questions}"
              f"\nTIME TO COMPLETE: {self.time_to_complete:02}:00 minutes!")

    @property
    def unique_test_number(self):
        return self._unique_test_number

    def delete_question(self, index):
        self._questions.pop(index)

    def delete_all_questions(self):
        self._questions.clear()

    def change_time_to_complete(self, new_time):
        self.time_to_complete = new_time

    def change_theme(self, new_theme):
        self.theme = new_theme


if __name__ == '__main__':
    question1 = Question("What is my name?")
    question1.add_answer("Reni")
    question1.add_answer("Beni")
    question1.add_answer("Teni")
    question1.set_correct_answer(0)

    question2 = Question("How old am I?")
    question2.add_answer("30")
    question2.add_answer("28")
    question2.add_answer("32")
    question2.set_correct_answer(2)

    test = TestContent("About me!", 2)
    test.add_question(question1)
    test.add_question(question2)

    test.read_questions_from_file_and_save_it()
    test.short_info()
    print(f"Unique test number is: {test.unique_test_number}")
    test.start_test()
    test.info()
