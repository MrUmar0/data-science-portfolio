Student Grade Tracker 📊

A simple Python script that reads student marks from a CSV file, calculates totals, averages, percentages, grades, and ranks, then exports a full results report — built using pandas and numpy.

Features


📥 Reads student data from students.csv
➕ Calculates Total, Average, and Percentage across 5 subjects
🏷️ Assigns a Grade (A+, A, B, C, D, F) based on percentage
✅ Marks each student as Pass or Fail
🏆 Ranks students by percentage (1 = highest)
📈 Generates subject-wise summary statistics (mean, max, min, std)
🥇 Shows the Top 3 and Bottom 3 performers
📊 Shows grade distribution (how many students got each grade)
💾 Saves the final results to student_results.csv


Subjects Tracked

SubjectMathScienceEnglishHistoryComputer

Each subject is assumed to be out of 100 marks, so the total is out of 500.

Grading Scale

PercentageGrade≥ 90%A+≥ 80%A≥ 70%B≥ 60%C≥ 50%D< 50%F

Pass/Fail is determined separately: a student needs more than 50% to be marked Pass.

File Structure

student-grade-tracker/
├── grade_tracker.py     # Main script
├── students.csv         # Input data (raw marks)
├── results.csv          # (optional) additional results file
└── README.md            # Project documentation


Note: the script writes its output to student_results.csv. Make sure this matches the filename you expect, or update the script/repo accordingly.



Requirements


Python 3.x
pandas
numpy


Install dependencies:

bashpip install pandas numpy

Input Format (students.csv)

The CSV should contain a Name column plus one column per subject:

csvName,Math,Science,English,History,Computer
Aarav,85,90,78,88,92
Diya,70,65,80,75,69
...

How to Run

bashpython grade_tracker.py

This will:


Print the raw student data
Print subject-wise summary statistics
Print grade distribution
Print the top 3 and bottom 3 ranked students
Save the complete results (with Total, Average, Percentage, Grade, Status, Rank) to student_results.csv


Sample Output Columns

NameMathScienceEnglishHistoryComputerTotalAveragePercentageGradesStatusRank

Possible Improvements


Align the Pass/Fail threshold with the grading scale (currently Pass requires > 50%, while grade D starts at >= 50%, so a student with exactly 50% would be graded D but marked Fail).
Add input validation for missing or out-of-range marks.
Add a bar chart of grade distribution using matplotlib (ties in nicely with the matplotlib/ folder in this repo!).
Allow subject list and max marks to be configurable instead of hardcoded.


Author

Part of the data-science practice repo — pandas & numpy exercises.