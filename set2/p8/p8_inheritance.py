# Name: Manangan, Adrian Romeo D.
# Section: IV-BSIT C
# Activity: P8 - Inheritance and Polymorphism
# Date: November 24, 2026


class Person:
    """Store information shared by people in the school."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")


class Student(Person):
    """A person enrolled in a course and section."""

    def __init__(self, name, age, student_id, course_section):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_section = course_section

    def introduce(self):
        print(
            f"I am student {self.name}, ID {self.student_id}, "
            f"from {self.course_section}."
        )


class Teacher(Person):
    """A person who teaches a subject."""

    def __init__(self, name, age, subject, years_experience):
        super().__init__(name, age)
        self.subject = subject
        self.years_experience = years_experience

    def introduce(self):
        print(
            f"I am teacher {self.name}; I teach {self.subject} and have "
            f"{self.years_experience} years of experience."
        )


def main():
    people = [
        Student("Alexandra Santos", 20, "2026001", "BSIT-2A"),
        Teacher("Maria Cruz", 35, "Python Programming", 10),
        Student("Benjamin Reyes", 21, "2026002", "BSIT-2B"),
    ]
    for person in people:
        person.introduce()


if __name__ == "__main__":
    main()


# Student and Teacher inherit the shared name, age, and initialization behavior from Person.
# Each child class calls super().__init__() and adds attributes specific to its role.
# Both child classes override introduce() to present their own information.
# The people list contains different object types, and the same method call produces role-specific output.
