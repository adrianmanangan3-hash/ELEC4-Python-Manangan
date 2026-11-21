# Name: Adrian Romeo D. Manangan
# Section: IV-BSIT C
# Activity: P2 - Student Utilities Main Program
# Date: November 21, 2026

import student_utils
from student_utils import calculate_average
from datetime import datetime


def read_grades():
    """Read and validate grades entered by the user."""
    grades = []
    while True:
        try:
            count = int(input("How many grades: "))
            if count > 0:
                break
            print("Enter at least one grade.")
        except ValueError:
            print("Invalid count.")

    for index in range(1, count + 1):
        while True:
            try:
                grade = float(input(f"Grade {index}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Grade must be from 0 to 100.")
            except ValueError:
                print("Invalid grade.")
    return grades


def main():
    print("Adrian Romeo D. Manangan - IV-BSIT C")
    grades = read_grades()
    print("\nStudent Grade Report")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Status: {student_utils.determine_status(grades)}")
    print(f"Highest: {student_utils.get_highest(grades):.2f}")
    print(f"Lowest: {student_utils.get_lowest(grades):.2f}")
    print("Generated:", datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"))


if __name__ == "__main__":
    main()
