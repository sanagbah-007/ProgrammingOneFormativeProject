# main.py
# This file provides the user-facing command-line interface (CLI) 
# for the Grade Tracker.It handles menu navigation, 
# user input validation, and connects user choices to the GradeTracker engine.

from abc import ABC, abstractmethod
from datetime import datetime
from models import Assignment, Homework, Exam
from tracker import GradeTracker

class not_empty_input(ABC):
    @abstractmethod
    def __call__(self, prompt):
        #Prompt for input and ensure it is not empty.
        pass

class NonEmptyInputValidator(not_empty_input):
    def __call__(self, prompt):
        while True:
            user_input = input(prompt).strip()
            if user_input:
                return user_input
            print("[!] Input cannot be empty. Please try again.")

not_empty_input = NonEmptyInputValidator()

def positive_float_input(prompt):
    # Prompt the user for a float input and validate it.
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
            else:
                print("[!] Please enter 0 or a positive number.")
        except ValueError:
            print("[!] Invalid input. Please enter a valid number.")

def validate_date(date_str):
    # Validate the date format (YYYY-MM-DD).
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_assignment(tracker):
    # Function to add a new assignment to the tracker.
    print("\n[+] Add a new assignment")
    subject = not_empty_input("Enter subject: ")
    title = not_empty_input("Enter title: ")
    score = positive_float_input("Enter score: ")

    # Validation loop to ensure score doesn't exceed max score
    while True:
        max_score = positive_float_input("Enter max score: ")
        if max_score >= score:
            break
        print("[!] Max score cannot be less than earned score.")

    due_date = not_empty_input("Enter due date (YYYY-MM-DD): ")
    while not validate_date(due_date):
        print("[!] Invalid date format. Please enter date in YYYY-MM-DD.")
        due_date = not_empty_input("Enter due date (YYYY-MM-DD): ")

    # Prompt for assignment type and validate it.
    while True:
        assignment_type = not_empty_input("Enter assignment type (homework/exam): ").lower()
        if assignment_type in ["homework", "exam"]:
            break
        print("[!] Invalid assignment type. Please enter 'homework' or 'exam'.")

    # Create the appropriate assignment object based on the type.
    if assignment_type == "homework":
        assignment = Homework(subject, title, score, max_score, due_date)
    else:
        assignment = Exam(subject, title, score, max_score, due_date)

    tracker.add_assignment(assignment)

def filter_assignments(tracker):
    # Function to filter assignments based on user input.
    print("\n[/] Filter assignments")
    print("1. By subject")
    print("2. By assignment type")
    print("3. By month (YYYY-MM)")
    choice = not_empty_input("Choose a filter option (1-3): ").strip()

    if choice == "1":
        subject = not_empty_input("Enter subject to filter by: ")
        filtered = tracker.filter_assignments(subject=subject)
    elif choice == "2":
        assignment_type = not_empty_input("Enter assignment type to filter by (homework/exam): ").lower()
        filtered = tracker.filter_assignments(assignment_type=assignment_type)
    elif choice == "3":
        month = not_empty_input("Enter month to filter by (YYYY-MM): ")
        while not validate_date(f"{month}-01"):
            print("[!] Invalid date format. Please enter month in YYYY-MM.")
            month = not_empty_input("Enter month to filter by (YYYY-MM): ")
        filtered = tracker.filter_assignments(month=month)
    else:
        print("[!] Invalid choice. Please enter a number between 1 and 3.")
        return

    tracker.assignments_list(filtered)

def main():
    # Main function to run the Grade Tracker CLI.
    tracker = GradeTracker()

    while True:
        print("\n=== Grade Tracker Menu ===")
        print("1. Add Assignment")
        print("2. View All Assignments")
        print("3. Filter Assignments")
        print("4. View Summary")
        print("0. Exit")

        choice = not_empty_input("Choose an option (0-4): ").strip()

        if choice == "1":
            add_assignment(tracker)
        elif choice == "2":
            tracker.assignments_list()
        elif choice == "3":
            filter_assignments(tracker)
        elif choice == "4":
            tracker.summary()
        elif choice == "0":
            print("[~] Exiting Grade Tracker!")
            break
        else:
            print("[!] Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()  



