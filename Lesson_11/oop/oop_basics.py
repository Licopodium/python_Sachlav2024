class TestClass:
    test_field = 36
    test_text = "hello"

    def __init__(self, name: str = "unknown", age: int = 18):
        self.name = name
        self.age = age

    def __int__(self):
        pass

    def get_info(self):
        print(self.age)
        print(self.name)


test_class = TestClass(age=36, name="Alex")
# print(test_class.test_field)
# print(test_class.test_text)
test_class.get_info()

test_2 = TestClass("Alexander", 45)
test_2.get_info()