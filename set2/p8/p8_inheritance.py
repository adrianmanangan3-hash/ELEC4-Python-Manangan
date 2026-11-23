# Name: Manangan, Adrian Romeo D.
# Section: IV-BSIT C
# Activity: P8 - Inheritance and Polymorphism
# Date: November 23, 2026


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def introduce(self):
        print(
            f"I am {self.name}, a {self.course} student "
            f"(ID: {self.student_id}), age {self.age}."
        )


class Teacher(Person):
    def __init__(self, name, age, subject, years_experience):
        super().__init__(name, age)
        self.subject = subject
        self.years_experience = years_experience

    def introduce(self):
        print(
            f"I am {self.name}, I teach {self.subject}, "
            f"and have {self.years_experience} years of experience."
        )


def main():
    people = [
        Person("Alex Morgan", 35),
        Student("Alyssa Santos", 20, "2026-001", "BSIT"),
        Teacher("Maria Rivera", 42, "Python Programming", 15),
    ]
    for person in people:
        person.introduce()


if __name__ == "__main__":
    main()


# Student and Teacher inherit the shared name, age, and constructor behavior from Person.
# Each child uses super().__init__() and adds attributes specific to its role.
# Both child classes override introduce() to provide their own role-specific message.
# The people list contains different object types, yet the same method call runs the correct version.
