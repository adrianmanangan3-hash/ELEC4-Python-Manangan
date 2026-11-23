# Name: Manangan, Adrian Romeo D.
# Section: IV-BSIT C
# Activity: P6 - Recursion Toolkit
# Date: November 23, 2026


# Base case: n is 0 or 1. Recursive call: n * factorial(n - 1).
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is defined here only for non-negative integers.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Base case: n is 0 or 1. Recursive call: fibonacci(n - 1) + fibonacci(n - 2).
def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci index must be a non-negative integer.")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: n is 0. Recursive call: n + sum_numbers(n - 1).
def sum_numbers(n):
    if n < 0:
        raise ValueError("Enter a non-negative integer.")
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base case: the list is empty. Recursive call: search the remaining list.
def search(items, target):
    if not items:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def read_non_negative_integer(prompt):
    try:
        value = int(input(prompt))
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        print("Enter a non-negative whole number.")
        return None


def show_menu():
    print("\nRECURSION TOOLKIT")
    print("1. Factorial")
    print("2. Fibonacci")
    print("3. Sum from 1 to n")
    print("4. Search a list")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            number = read_non_negative_integer("Enter n: ")
            if number is not None:
                print(f"{number}! = {factorial(number)}")
        elif choice == "2":
            number = read_non_negative_integer("Enter the number of terms n: ")
            if number is not None:
                terms = [fibonacci(index) for index in range(number)]
                print(f"Fibonacci number at index {number}: {fibonacci(number)}")
                print(f"First {number} term(s): {terms}")
        elif choice == "3":
            number = read_non_negative_integer("Enter n: ")
            if number is not None:
                print(f"Sum from 1 to {number}: {sum_numbers(number)}")
        elif choice == "4":
            items = [item.strip() for item in input("Enter comma-separated items: ").split(",")]
            target = input("Enter the value to search for: ").strip()
            print(f"Found: {search(items, target)}")
        elif choice == "5":
            print("Exiting Recursion Toolkit.")
            break
        else:
            print("Invalid menu choice. Choose 1 to 5.")


if __name__ == "__main__":
    print("Adrian Romeo D. Manangan - IV-BSIT C")
    main()
