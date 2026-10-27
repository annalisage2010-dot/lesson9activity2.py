class student:
    grade = 11
    name = "Anna"

    def introduction(self):
        print("Hello! I am a student")

    def details(self):
        print("Hi! My name is", self.name)
        print("I am in grade", self.grade)

object = student()
object.introduction()
object.details()