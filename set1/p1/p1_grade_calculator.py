# Name: Manangan, Adrian Romeo D.
# Section: IV-BSIT C
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026


def accept_grades():
    """Accept a list of validated numeric grades from the user."""
    while True:
        try:
            count = int(input("Enter the number of grades: "))
            if count <= 0:
                print("Please enter at least one grade.")
                continue
            break
        except ValueError:
            print("Invalid number. Enter a whole number.")

    grades = []
    for index in range(1, count + 1):
        while True:
            try:
                grade = float(input(f"Enter grade {index}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Invalid grade. Enter a number from 0 to 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
    return grades


def compute_average(grades):
    """Compute and return the average grade."""
    return sum(grades) / len(grades)


def get_highest_grade(grades):
    """Return the highest grade."""
    return max(grades)


def get_lowest_grade(grades):
    """Return the lowest grade."""
    return min(grades)


def determine_status(grades):
    """Return PASS or FAIL based on the passing average."""
    return "PASS" if compute_average(grades) >= 75 else "FAIL"


def display_results(grades):
    """Display all computed grade results."""
    if not grades:
        print("\nNo grades entered yet.")
        return
    print("\nGrade Results:")
    print(f"Average: {compute_average(grades):.2f}")
    print(f"Highest: {get_highest_grade(grades):.2f}")
    print(f"Lowest: {get_lowest_grade(grades):.2f}")
    print(f"Status: {determine_status(grades)}")


def show_menu():
    print("\nSTUDENT GRADE CALCULATOR")
    print("1. Enter grades")
    print("2. View results")
    print("3. Exit")


def main():
    grades = []
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            grades = accept_grades()
            print("Grades saved.")
        elif choice == "2":
            display_results(grades)
        elif choice == "3":
            print("Exiting student grade calculator.")
            break
        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    print("Adrian Romeo D. Manangan - IV-BSIT C")
    main()


# A local variable is created inside a function and only exists in that function.
# In this program, grades inside main is local to main and holds the saved grade list.
# Parameters such as grades in compute_average are also local variables.
# A global variable is declared outside all functions and can be used throughout the module.
# This program avoids global variables so each grade list is controlled within main.
