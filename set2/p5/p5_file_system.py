# Name: Manangan, Adrian Romeo D.
# Section: IV-BSIT C
# Activity: P5 - Student Information File System
# Date: November 24, 2026

from pathlib import Path
import math


DATA_FILE = Path(__file__).resolve().with_name("students.txt")


def load_students():
    """Load valid student records; a missing file starts with no records."""
    students = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                fields = line.rstrip("\n").split("|")
                if len(fields) != 4:
                    print(f"Skipping malformed record on line {line_number}.")
                    continue
                student_id, name, course_section, average_text = fields
                try:
                    average = float(average_text)
                    if not math.isfinite(average) or not 0 <= average <= 100:
                        raise ValueError
                except ValueError:
                    print(f"Skipping invalid average on line {line_number}.")
                    continue
                students.append({
                    "student_id": student_id,
                    "name": name,
                    "course_section": course_section,
                    "average": average,
                })
    except FileNotFoundError:
        return []
    except OSError as error:
        print(f"Could not read student records: {error}")
    return students


def save_students(students):
    """Write all records to the data file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            for student in students:
                file.write(
                    f"{student['student_id']}|{student['name']}|"
                    f"{student['course_section']}|{student['average']:.2f}\n"
                )
    except OSError as error:
        print(f"Could not save student records: {error}")
        return False
    print("Student records saved.")
    return True


def read_required_text(prompt):
    """Read a non-empty field that fits the one-line file format."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("This field cannot be empty.")
        elif "|" in value or "\n" in value or "\r" in value:
            print("Do not use the | character or a line break.")
        else:
            return value


def read_average():
    """Read a numeric average between 0 and 100."""
    while True:
        try:
            average = float(input("General average (0-100): "))
            if math.isfinite(average) and 0 <= average <= 100:
                return average
            print("The average must be from 0 to 100.")
        except ValueError:
            print("Invalid average. Enter a number.")


def find_student(students, student_id):
    """Return a student matching an ID, or None."""
    return next(
        (student for student in students if student["student_id"] == student_id),
        None,
    )


def display_students(students):
    """Display every student record."""
    print("\nStudent Records")
    if not students:
        print("No student records found.")
        return
    for student in students:
        print(
            f"ID: {student['student_id']} | Name: {student['name']} | "
            f"Course/Section: {student['course_section']} | "
            f"General Average: {student['average']:.2f}"
        )


def add_student(students):
    """Collect and save a new student record."""
    student_id = read_required_text("Student ID: ")
    if find_student(students, student_id):
        print("That student ID already exists.")
        return
    student = {
        "student_id": student_id,
        "name": read_required_text("Full name: "),
        "course_section": read_required_text("Course/section: "),
        "average": read_average(),
    }
    students.append(student)
    if not save_students(students):
        students.pop()


def search_student(students):
    """Find and display a student by ID."""
    student_id = input("Enter student ID to search: ").strip()
    student = find_student(students, student_id)
    if student:
        display_students([student])
    else:
        print("Student not found.")


def update_student(students):
    """Update an existing student's information and save it."""
    student_id = input("Enter student ID to update: ").strip()
    student = find_student(students, student_id)
    if not student:
        print("Student not found.")
        return

    updated = {
        "student_id": student_id,
        "name": read_required_text("New full name: "),
        "course_section": read_required_text("New course/section: "),
        "average": read_average(),
    }
    old_values = student.copy()
    student.update(updated)
    if not save_students(students):
        student.update(old_values)


def show_menu():
    print("\nSTUDENT INFORMATION FILE SYSTEM")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search by ID")
    print("4. Update student")
    print("5. Exit")


def main():
    students = load_students()
    print(f"Loaded {len(students)} student record(s).")
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            print("Exiting Student Information File System.")
            break
        else:
            print("Invalid menu choice. Choose 1-5.")


if __name__ == "__main__":
    main()
