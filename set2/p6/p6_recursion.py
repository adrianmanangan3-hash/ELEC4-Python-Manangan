# Name: Manangan, Adrian Romeo D.
# Section: IV-BSIT C
# Activity: P6 - Recursion Toolkit
# Date: November 24, 2026

from functools import lru_cache


# Base case: 0! is 1. Recursive call: n * factorial(n - 1).
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Base cases: F(0) is 0 and F(1) is 1. Recursive call: F(n - 1) + F(n - 2).
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: the sum through 0 is 0. Recursive call: n + sum_numbers(n - 1).
def sum_numbers(n):
    if n <= 0:
        return 0
    return n + sum_numbers(n - 1)


# Base case: an empty list has no target. Recursive call: search the remaining list.
def search(items, target):
    if not items:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def read_nonnegative_integer(prompt):
    """Read a nonnegative integer while handling invalid input."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Enter a nonnegative integer.")
        except ValueError:
            print("Invalid input. Enter a whole number.")


def show_menu():
    print("\nRECURSION TOOLKIT")
    print("1. Factorial")
    print("2. Fibonacci and first n terms")
    print("3. Sum from 1 to n")
    print("4. Search a list")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            number = read_nonnegative_integer("Enter n: ")
            print(f"{number}! = {factorial(number)}")
        elif choice == "2":
            count = read_nonnegative_integer("How many Fibonacci terms: ")
            terms = [fibonacci(index) for index in range(count)]
            print(f"First {count} term(s): {terms}")
            if count:
                print(f"Fibonacci number at index {count - 1}: {fibonacci(count - 1)}")
        elif choice == "3":
            number = read_nonnegative_integer("Enter n: ")
            print(f"Sum from 1 to {number}: {sum_numbers(number)}")
        elif choice == "4":
            items = input("Enter list values separated by commas: ").split(",")
            items = [item.strip() for item in items if item.strip()]
            target = input("Enter target value: ").strip()
            print(f"Target found: {search(items, target)}")
        elif choice == "5":
            print("Exiting Recursion Toolkit.")
            break
        else:
            print("Invalid menu choice. Choose 1-5.")


if __name__ == "__main__":
    main()
