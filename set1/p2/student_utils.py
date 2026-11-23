# Name: Manangan, Adrian Romeo D.
# Section: IV-BSIT C
# Activity: P2 - Student Utilities Module
# Date: November 21, 2026


def calculate_average(grades):
    """Calculate the average of a grade list."""
    return sum(grades) / len(grades)


def determine_status(grades):
    """Determine pass or fail using a 75-point average."""
    return "PASS" if calculate_average(grades) >= 75 else "FAIL"


def get_highest(grades):
    """Return the highest grade."""
    return max(grades)


def get_lowest(grades):
    """Return the lowest grade."""
    return min(grades)
