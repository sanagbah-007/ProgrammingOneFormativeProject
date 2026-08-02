# tracker.py
# This file contains the main engine of the grade tracker project.
# It sets up a class to store assignments in memory and provides 
# methods to add, display, filter, and summarize student grades.

# Foundational class: handles assignment collection, list filtering, and summary calculations.
class GradeTracker:
    def __init__(self):
        # Set up an empty list to store assignments
        self.assignments = []

    def add_assignment(self, assignment):
        # Add a new assignment to the list
        self.assignments.append(assignment) 
        print("\n[+] Assignment successfully added!")

    def assignments_list(self, assignment_list = None):
        # Display a list of assignments in a formatted, readable table.
        if assignment_list is None:
            assignment_list = self.assignments
        if not assignment_list:
            print("\n[!] No assignments found.")
            return

        print("\n" + "=" * 65)
        print(f"{'Type':<10} | {'Subject':<12} | {'Title':<15} | {'Score':<8} | {'Due Date':<10}")
        print("=" * 65)

        for item in assignment_list:
            # Format score as score/max_score (e.g., 85/100)
            score_str = f"{item.score:.1f}/{item.max_score:.1f}"
            print(f"{item.type.capitalize():<10} | {item.subject.capitalize():<12} | {item.title:<15} | {score_str:<8} | {item.due_date:<10}")

        print("=" * 65)

    def filter_assignments(self, subject=None, assignment_type=None, month=None):
        # Filter assignments based on subject, assignment type, and month.
        filtered = self.assignments
        if subject:
            filtered = [item for item in filtered if item.subject.lower() == subject.strip().lower()]
        if assignment_type:
            filtered = [item for item in filtered if item.assignment_type.lower() == assignment_type.strip().lower()]
        if month:
            filtered = [item for item in filtered if item.due_date.startswith(month.strip())]
        return filtered

    def summary(self):
        # Calculate and display the total score, total max score, and overall percentage.
        if not self.assignments:
            print("\n[!] No assignments found.")
            return
        
        # Overall summary calculations
        total_score = sum(item.score for item in self.assignments)
        total_max_score = sum(item.max_score for item in self.assignments)
        overall_percentage = (total_score / total_max_score * 100) if total_max_score > 0 else 0.0

        print("\n" + "=" * 40)
        print(f"{'Total Score:':<20} {total_score:.1f}")
        print(f"{'Total Max Score:':<20} {total_max_score:.1f}")
        print(f"{'Overall Percentage:':<20} {overall_percentage:.2f}%")
        print("=" * 40)

        # Subject-wise summary calculations
        subjects_summary = {}
        for item in self.assignments:
            if item.subject not in subjects_summary:
                subjects_summary[item.subject] = {'score': 0, 'max_score': 0}
            subjects_summary[item.subject]['score'] += item.score
            subjects_summary[item.subject]['max_score'] += item.max_score
            
        print(f"\nSubject Summary:")
        for subject, summary in subjects_summary.items():
            subject_percentage = (summary['score'] / summary['max_score'] * 100) if summary['max_score'] > 0 else 0.0
            print(f"  {subject.capitalize()}: {summary['score']:.1f}/{summary['max_score']:.1f} ({subject_percentage:.2f}%)")

        # Highest and lowest scoring assignments
        highest_assignment = max(self.assignments, key=lambda x: x.get_percentage(), default=None)
        lowest_assignment = min(self.assignments, key=lambda x: x.get_percentage(), default=None)
        if highest_assignment:
            print(f"\nHighest Scoring Assignment: {highest_assignment.title} ({highest_assignment.subject.capitalize()}) ({highest_assignment.get_percentage():.2f}%)") 
        if lowest_assignment:
            print(f"Lowest Scoring Assignment: {lowest_assignment.title} ({lowest_assignment.subject.capitalize()}) ({lowest_assignment.get_percentage():.2f}%)")
            print("=" * 40)



