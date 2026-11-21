# Name: Adrian Romeo D. Manangan
# Section: IV-BSIT C
# Activity: P4 - Safe Menu Program
# Date: November 21, 2026


def read_number(prompt):
    """Read a number and translate invalid text into a clear message."""
    return float(input(prompt))


def division_option():
    """Perform division with handled input and zero-division errors."""
    try:
        numerator = read_number("Enter the first number: ")
        denominator = read_number("Enter the second number: ")
        result = numerator / denominator
    except ValueError:
        print("Error: Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result:.2f}")
    finally:
        print("Division operation finished.")


def open_file_option():
    """Open and display a text file, handling missing files."""
    file_name = input("Enter file name: ").strip()
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    else:
        print("File contents:")
        print(contents)
    finally:
        print("Open-file operation finished.")


def show_menu():
    print("\nSAFE MENU PROGRAM")
    print("1. Division")
    print("2. Open file")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            division_option()
        elif choice == "2":
            open_file_option()
        elif choice == "3":
            print("Exiting Safe Menu Program.")
            break
        else:
            print("Invalid menu choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    print("Adrian Romeo D. Manangan - IV-BSIT C")
    main()
