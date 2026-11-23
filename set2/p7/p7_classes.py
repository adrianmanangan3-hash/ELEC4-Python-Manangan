# Name: Manangan, Adrian Romeo D.
# Section: IV-BSIT C
# Activity: P7 - Student Management System with Classes
# Date: November 23, 2026


class Student:
    def __init__(self, student_id, name, course, grade):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.__grade = None
        self.set_grade(grade)

    def display_info(self):
        print(
            f"{self.student_id} | {self.name} | {self.course} | "
            f"General average: {self.get_grade():.2f}"
        )

    def update_info(self, name=None, course=None):
        if name:
            self.name = name
        if course:
            self.course = course

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            raise ValueError("Grade must be a number from 0 to 100.")
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be from 0 to 100.")
        self.__grade = float(grade)


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def display_info(self):
        print(f"{self.name} - Teacher: {self.teacher}")


class Section:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        print(f"\nSection: {self.name}")
        print(f"Subject: {self.subject.name} (Teacher: {self.subject.teacher})")
        for student in self.students:
            student.display_info()


def main():
    programming = Subject("Python Programming", "Ms. Rivera")
    section = Section("IV-BSIT C", programming)

    students = [
        Student("2026-001", "Alyssa Santos", "BSIT", 92.5),
        Student("2026-002", "Brandon Reyes", "BSIT", 88.75),
        Student("2026-003", "Camila Garcia", "BSIT", 95.0),
    ]
    for student in students:
        section.add_student(student)

    students[1].update_info(name="Brandon Reyes-Santos")
    students[1].set_grade(90.0)
    print("Updated one student's name and grade.")
    section.list_students()


if __name__ == "__main__":
    main()
