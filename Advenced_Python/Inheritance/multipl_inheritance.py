class Father():
    def skill(self):
        print("gardening")
class Mother():
    def skill(self):
        print("cooking")

class child(Father,Mother):
    def sp(self):
        Mother.skill(self)
        Father.skill(self)
        print("sport")
c = child()

c.sp()
#exercice
class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is a person")

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} was a student and now I'm still a student")

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} was a student and now I'm a teacher")

class Youtuber(Person):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} was a student and now I'm a YouTuber")

class TeacherYoutuber(Teacher, Youtuber):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} is both a teacher and a YouTuber")

t = Teacher("Alice")
y = Youtuber("Bob")
ty = TeacherYoutuber("Charlie")
s = Student("David")
