# Student Grade Tracker
 A simple command-line tool built in Python 3 that helps students track 
homework and exam grades, view assignment lists, filter results, 
and calculate summary statistics during a study session.


## Project Overview & Features
 The Student Grade Tracker keeps all data in memory while running, making 
it fast and easy to use without cluttering your local machine with temporary files.

## Key Features:
- Add Assignments: Record both Homework and Exam tasks with scores, max scores, due dates, and subjects.
- View Assignments: Display all saved assignments in a clean table.
- Filter Assignments: Search through assignments by subject name, task type (homework or exam), or month (YYYY-MM).
- Grade Summaries: View overall percentage averages, per-subject breakdowns, and see your highest and lowest scoring tasks.


## Project File Structure
- models.py: Contains the Assignment base class and the Homework and Exam subclasses.
- tracker.py: Contains the GradeTracker manager class that stores assignments in memory and performs calculations.
- main.py: Runs the interactive terminal menu and validates user inputs.


## How to Run the Program
1. Make sure Python 3 is installed on your computer.
2. Open your terminal or command prompt and navigate to the project directory:
        cd path/to/project 
3. Run the main script:
        python main.py

## Menu Structure
When you launch the program, you will see the following menu:

 === Grade Tracker Menu ===
 1. Add Assignment
 2. View All Assignments
 3. Filter Assignments
 4. View Summary
 0. Exit

   ![alt text](MenuStructure.png)

## Sample Interaction
1. Adding an Assignment

 [+] Add a new assignment
 Enter subject: Maths
 Enter title: Algebra Quiz
 Enter score: 18
 Enter max score: 20
 Enter due date (YYYY-MM-DD): 2025-10-15
 Enter assignment type (homework/exam): homework

 [+] Assignment successfully added!

   ![alt text](AddAssignment.png)


2. Viewing All Assignments

 ======================================================================
 Type       | Subject      | Title           | Score    | Due Date  
 ======================================================================
 Homework   | Maths        | Algebra Quiz    | 18.0/20.0 | 2025-10-15
 ======================================================================

   ![alt text](ViewAssignment.png)


3. Summary Output

 ========================================
 Total Score:         18.0
 Total Max Score:     20.0
 Overall Percentage:  90.00%
 ========================================

 Subject Summary:
   Maths: 18.0/20.0 (90.00%)

 Highest Scoring Assignment: Algebra Quiz (Maths) (90.00%)
 Lowest Scoring Assignment: Algebra Quiz (Maths) (90.00%)
 ======================================================================

   ![alt text](SummaryOutput.png)


4. Filter Output


 [/] Filter assignments
 1. By subject
 2. By assignment type
 3. By month (YYYY-MM)
 Choose a filter option (1-3): 1
 Enter subject to filter by: maths

 ======================================================================
 Type       | Subject      | Title           | Score    | Due Date  
 ======================================================================
 Homework   | Maths        | Algebra Quiz    | 18.0/20.0 | 2025-10-15
 ======================================================================

   ![alt text](FilterOutput.png)


