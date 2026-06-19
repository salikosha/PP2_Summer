class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_info(self):
        super().show_info()
        print(f"Student ID: {self.student_id}")



x = Student("Sabinka", 20, "22B050857")
x.show_info()
