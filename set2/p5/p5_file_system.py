# Name: Manangan, Adrian Romeo D.
# Section: IV-BSIT C
# Activity: P5 - Student Information File System
# Date: November 23, 2026

import csv
import math
from dataclasses import dataclass
from pathlib import Path


STUDENTS_FILE = Path(__file__).with_name("students.txt")


@dataclass
class StudentRecord:
    student_id: str
    full_name: str
    course_section: str
    average: float


def load_students():
    """Load student records, continuing with an empty list if no file exists."""
    students = []
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8", newline="") as file:
            for line_number, row in enumerate(csv.reader(file, delimiter="|"), start=1):
                if len(row) != 4:
                    print(f"Skipping malformed record on line {line_number}.")
                    continue
                try:
                    average = float(row[3])
                except ValueError:
                    print(f"Skipping record with an invalid average on line {line_number}.")
                    continue
                students.append(StudentRecord(row[0], row[1], row[2], average))
    except FileNotFoundError:
        pass
    except OSError as error:
        print(f"Could not read {STUDENTS_FILE.name}: {error}")
    return students


def save_students(students):
    """Write all student records to the text file."""
    try:
        with open(STUDENTS_FILE, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter="|", lineterminator="\n")
            for student in students:
                writer.writerow(
                    (
                        student.student_id,
                        student.full_name,
                        student.course_section,
                        f"{student.average:.2f}",
                    )
                )
    except OSError as error:
        print(f"Could not save {STUDENTS_FILE.name}: {error}")
        return False
    return True


def read_average(prompt, current_value=None):
    """Read an average from 0 to 100, allowing a blank to retain an old value."""
    while True:
        value = input(prompt).strip()
        if not value and current_value is not None:
            return current_value
        try:
            average = float(value)
            if math.isfinite(average) and 0 <= average <= 100:
                return average
            print("Enter a finite average from 0 to 100.")
        except ValueError:
            print("Invalid average. Enter a number from 0 to 100.")


def find_student(students, student_id):
    """Return a student matching the exact ID, if present."""
    return next((student for student in students if student.student_id == student_id), None)


def add_student(students):
    student_id = input("Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if find_student(students, student_id):
        print("A student with that ID already exists.")
        return

    full_name = input("Full name: ").strip()
    course_section = input("Course/section: ").strip()
    if not full_name or not course_section:
        print("Name and course/section cannot be empty.")
        return
    average = read_average("General average: ")
    students.append(StudentRecord(student_id, full_name, course_section, average))
    if save_students(students):
        print("Student record added and saved.")


def display_students(students):
    if not students:
        print("No student records found.")
        return
    print("\nSTUDENT RECORDS")
    for student in students:
        print(
            f"ID: {student.student_id} | Name: {student.full_name} | "
            f"Course/Section: {student.course_section} | Average: {student.average:.2f}"
        )


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()
    student = find_student(students, student_id)
    if student:
        display_students([student])
    else:
        print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()
    student = find_student(students, student_id)
    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")
    full_name = input(f"Full name [{student.full_name}]: ").strip()
    course_section = input(f"Course/section [{student.course_section}]: ").strip()
    average = read_average(
        f"General average [{student.average:.2f}]: ",
        current_value=student.average,
    )
    if full_name:
        student.full_name = full_name
    if course_section:
        student.course_section = course_section
    student.average = average
    if save_students(students):
        print("Student record updated and saved.")


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
            print("Invalid menu choice. Choose 1 to 5.")


if __name__ == "__main__":
    print("Adrian Romeo D. Manangan - IV-BSIT C")
    main()
