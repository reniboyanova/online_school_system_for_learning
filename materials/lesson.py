
unique_lesson_numbers = []


class LessonContent:
    def __init__(self, theme: str, title: str, content: str):
        self.theme = theme
        self.title = title
        self.content = content
        self._unique_lesson_number = 0

    def short_info(self):
        short_content_info_len = int(len(self.content) / 5)
        short_content = self.content[:short_content_info_len]
        print(f"THEME: {self.theme}\nTITLE: {self.title}\nABOUT: {short_content}...\n")


if __name__ == '__main__':
    lesson = LessonContent(str(input("Insert lesson theme: ")),
                               str(input("Insert lesson title: ")), str(input("Insert content: ")))

    lesson.short_info()