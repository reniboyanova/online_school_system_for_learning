class News:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def short_info(self):
        short_content_len = int(len(self.content) / 5)
        print(f"TITLE: {self.title}\nCONTENT: {self.content[:short_content_len]}...\n")

