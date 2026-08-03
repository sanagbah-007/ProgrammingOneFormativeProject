# models.py
# This file contains the blueprint of the grade tracker project.
# It sets up a base class for general assignment attributes and 
# uses inheritance to create specific subclasses for homework tasks and exam tasks.


# Base class: holds the subject name, task title, max_score, due_date and assignment_type.
class Assignment:
    def __init__(self, subject, title, score, max_score, due_date, assignment_type):
        self.assignment_type = assignment_type.strip().lower()  # Convert assignment type to lowercase

        self.subject = subject.strip().lower()  # so 'Physics' and 'physics' are treated the same.
        self.title = title.strip()
       
        self.score = float(score)  # Convert score to float for accuracy in calculations.
        self.max_score = float(max_score)

        self.due_date = due_date.strip()  # Saves the due date string in 'YYYY-MM-DD' format.

    def get_percentage(self):
        # Calculates and returns the percentage score for the assignment.
        if self.max_score == 0:
            return 0.0  # Avoid division by zero
        return (self.score / self.max_score) * 100

# Subclass, Homework, inheriting from Assignment.
class Homework(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, assignment_type ="homework") 
        # Calls the base class constructor with the attributes specific to homework.


# Subclass, Exam, inheriting from Assignment.
class Exam(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, assignment_type ="exam") 
        # Calls the base class constructor with the attributes specific to exams.







        