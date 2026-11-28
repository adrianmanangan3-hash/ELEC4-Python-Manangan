# Name: Manangan, Adrian Romeo D.
# Section: IV-BSIT C
# Activity: P7 - Student Management System with Classes
# Date: November 24, 2026


class Subject:
    """Represent a subject offered by the school."""

    def __init__(self, code, title):
        self.code = code
        self.title = title

    def __str__(self):
        return f"{self.code} - {self.title}"


class Student:
    """Represent a student and protect the student's grade."""

    def __init__(self, student_id, name, course_section, grade):
        self.student_id = student_id
        self.name = name
        self.course_section = course_section
        self.__grade = None
        self.set_grade(grade)

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        """Set a valid numeric grade from 0 to 100."""
        try:
            grade = float(grade)
        except (TypeError, ValueError) as error:
            raise ValueError("Grade must be a number from 0 to 100.") from error
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be from 0 to 100.")
        self.__grade = grade

    def update_information(self, name, course_section, grade):
        self.set_grade(grade)
        self.name = name
        self.course_section = course_section

    def display(self):
        print(
            f"{self.student_id} | {self.name} | {self.course_section} | "
            f"Grade: {self.get_grade():.2f}"
        )


class Section:
    """Group students taking the same subject."""

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        print(f"\nSection {self.name} - {self.subject}")
        for student in self.students:
            student.display()


def main():
    programming = Subject("ITP101", "Introduction to Programming")
    section = Section("BSIT-2A", programming)

    students = [
        Student("2026001", "Alexandra Santos", section.name, 92.5),
        Student("2026002", "Benjamin Reyes", section.name, 88.75),
        Student("2026003", "Camila Garcia", section.name, 95),
    ]
    for student in students:
        section.add_student(student)

    students[1].update_information("Benjamin Reyes", section.name, 90.25)
    section.list_students()


if __name__ == "__main__":
    main()
