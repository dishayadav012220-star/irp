"""
Placement Readiness Tracker
IRP-II (CSE2596) Assignment - Task 1: data and control structures.
"""

# Each student is a dictionary; all students are stored in a list.
students = [
    {"name": "Aarav Sharma", "roll_no": 101, "aptitude": 82, "verbal": 76, "coding": 91},
    {"name": "Diya Verma",   "roll_no": 102, "aptitude": 64, "verbal": 70, "coding": 58},
    {"name": "Kabir Singh",  "roll_no": 103, "aptitude": 45, "verbal": 52, "coding": 38},
    {"name": "Meera Iyer",   "roll_no": 104, "aptitude": 30, "verbal": 35, "coding": 28},
    {"name": "Rohan Gupta",  "roll_no": 105, "aptitude": 90, "verbal": 85, "coding": 88},
]


def read_score(subject):
    """Keep asking until the user enters a whole number between 0 and 100."""
    while True:
        text = input(f"Enter {subject} score (0-100): ")
        try:
            score = int(text)              # input() gives str, so convert to int
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if 0 <= score <= 100:
            return score
        print("  Score must be between 0 and 100. Try again.")


def add_student_from_input(students):
    """Read one more student from the keyboard and add it to the list."""
    name = input("Enter student name: ").strip()
    while True:
        try:
            roll_no = int(input("Enter roll number: "))
            break
        except ValueError:
            print("  Roll number must be a number.")
    student = {
        "name": name,
        "roll_no": roll_no,
        "aptitude": read_score("aptitude"),
        "verbal": read_score("verbal"),
        "coding": read_score("coding"),
    }
    students.append(student)


def main():
    add_student_from_input(students)
    print(f"\nTotal students recorded: {len(students)}")


if __name__ == "__main__":
    main()
