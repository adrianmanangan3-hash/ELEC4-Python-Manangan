# Name: Adrian Romeo D. Manangan
# Section: IV-BSIT C
# Activity: P3 - Student Record Manager
# Date: November 21, 2026


def add_student(student_list, used_names, name):
    """Add a name only if a normalized copy is not already present."""
    normalized_name = " ".join(name.lower().split())
    if normalized_name in used_names:
        print("Duplicate entry: that student is already in the record.")
        return False

    display_name = " ".join(word.capitalize() for word in name.split())
    student_list.append(display_name)
    used_names.add(normalized_name)
    print(f"{display_name} added.")
    return True


def remove_student(student_list, used_names, name):
    """Remove a matching name case-insensitively."""
    normalized_name = " ".join(name.lower().split())
    for student in student_list:
        if " ".join(student.lower().split()) == normalized_name:
            student_list.remove(student)
            used_names.remove(normalized_name)
            print(f"{student} removed.")
            return
    print("Student not found.")


def search_students(student_list, search_text):
    """Return names containing the partial search text."""
    search_text = search_text.lower().strip()
    return [student for student in student_list if search_text in student.lower()]


def display_students(student_list):
    """Display the student list alphabetically with a total count."""
    print("\nStudent Records:")
    if not student_list:
        print("No students.")
    else:
        for number, student in enumerate(sorted(student_list, key=str.lower), start=1):
            print(f"{number}. {student}")
    print(f"Total: {len(student_list)}")


def show_menu():
    print("\nSTUDENT RECORD MANAGER")
    print("1. Add student")
    print("2. Remove student")
    print("3. Search student")
    print("4. Display all students")
    print("5. Exit")


def main():
    student_list = []
    used_names = set()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student(student_list, used_names, input("Enter student name: ").strip())
        elif choice == "2":
            remove_student(student_list, used_names, input("Enter name to remove: ").strip())
        elif choice == "3":
            search_text = input("Enter partial name: ").strip()
            results = search_students(student_list, search_text)
            if results:
                print("Search results:")
                for student in sorted(results, key=str.lower):
                    print(student)
            else:
                print("No matching student.")
        elif choice == "4":
            display_students(student_list)
        elif choice == "5":
            print("Exiting Student Record Manager.")
            break
        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    print("Adrian Romeo D. Manangan - IV-BSIT C")
    main()


# A list is an ordered collection that keeps the student names in a changeable sequence.
# This program stores display names in the student_list and uses the list for operations.
# A set is an unordered collection that is useful for fast membership checks and duplicate prevention.
# This program uses used_names as a set of normalized names so Juan Cruz and juan cruz are duplicates.
