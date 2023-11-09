
class AllTests:
    def __init__(self):
        self.tests = []

    def display(self):
        for test in self.tests:
            test.short_info()

    def delete_test(self, test_unique_index):
        for test in self.tests:
            if test.unique_test_number == test_unique_index:
                del test
                break

    def add_test(self, test):
        self.tests.append(test)

    def delete_all_test(self):
        self.tests.clear()



