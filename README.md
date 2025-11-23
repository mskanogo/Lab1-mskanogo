Grade Generator
A Python script for calculating student grades with weighted assignments across Formative (FA) and Summative (SA) categories.
Overview
This script is designed for African Leadership University's Introduction to Python Programming and Databases course (BSE Year 1, Trimester 2). It allows users to input multiple assignments, validates the data, calculates final grades and GPA, and exports all data to a CSV file.
Features

 Interactive command-line interface
 Input validation for grades, categories, and weights
 Weighted grade calculations
 Pass/fail determination based on category performance
 GPA calculation on a 5.0 scale
 Detailed console summary
 CSV export functionality

Requirements

Python 3.x
No external libraries required (uses built-in csv module)

Installation

Download the grade-generator.py file
Ensure Python 3 is installed on your system
No additional setup required!

Usage
Running the Script
bashpython grade-generator.py
Input Process
The script will prompt you to enter the following for each assignment:

Assignment Name: Any descriptive name (e.g., "Group Coding Lab")
Category:

FA for Formative Assessment
SA for Summative Assessment
(Case-insensitive: "fa", "FA", "Fa" all work)


Grade Obtained: A number between 0 and 100
Weight: A positive number representing the assignment's weight

After each assignment, you'll be asked: Add another assignment? (y/n):

Enter y to add more assignments
Enter n to finish and see results

Validation Rules
The script enforces the following validation rules:
InputRuleExample ErrorGradeMust be between 0-100"Error: Grade must be between 0 and 100."CategoryMust be "FA" or "SA""Error: Category must be 'FA' (Formative) or 'SA' (Summative)."WeightMust be a positive number"Error: Weight must be a positive number."Data TypesGrades and weights must be numbers"Error: Grade must be a valid number."
Calculation Logic
Weighted Grade
For each assignment:
Weighted Grade = (Grade / 100) × Weight
Category Totals
Total Formative (FA) = Sum of all FA weighted grades
Total Summative (SA) = Sum of all SA weighted grades
Final Grade and GPA
Total Grade = Total Formative + Total Summative
GPA = (Total Grade / 100) × 5.0
Pass/Fail Logic
A student passes only if they achieve at least 50% in BOTH categories:

If total FA weight is 60, student needs ≥ 30 points from FA assignments
If total SA weight is 40, student needs ≥ 20 points from SA assignments
Both conditions must be met to pass overall

Output
1. Console Summary
The script displays:

List of all assignments with their details
Weighted grade for each assignment
Category totals (FA and SA)
Pass/fail status for each category
Final grade out of 100
GPA out of 5.0
Overall pass/fail status

2. CSV File Export
A file named grades.csv is automatically created with the following format:
csvAssignment,Category,Grade,Weight
Group Coding Lab,FA,85,30
Midterm Exam,SA,78,40
Weekly Quiz,FA,92,10
Final Project,SA,88,20

File Structure
grade-generator.py
├── validate_grade()         # Validates grade input (0-100)
├── validate_category()      # Validates category (FA/SA)
├── validate_weight()        # Validates weight (positive number)
├── collect_assignment_data() # Interactive input collection
├── calculate_grades()       # Performs all calculations
├── print_summary()          # Displays results to console
├── export_to_csv()          # Exports data to CSV file
└── main()                   # Main program flow

CSV File Organizer (organizer.sh)
A Bash shell script that automatically archives CSV files with timestamps and maintains a detailed log of all operations.
Overview
This script is part of the African Leadership University Individual Coding Lab for Introduction to Python Programming and Databases (BSE Year 1, Trimester 2). It works alongside the grade-generator.py script to organize and preserve CSV output files.
Purpose
The organizer script:

Archives all CSV files in the current directory
Adds timestamps to filenames for version tracking
Logs all operations including file contents
Maintains a cumulative log across multiple runs

Requirements

Bash shell (Linux, macOS, or Git Bash on Windows)
Read/write permissions in the current directory

Installation

Download organizer.sh to your working directory
Make the script executable:

bash   chmod +x organizer.sh
Usage
Basic Execution
bash./organizer.sh
What Happens

Check/Create Archive Directory

Checks if an archive/ directory exists
Creates it if not present


Find CSV Files

Searches for all .csv files in the current directory
Excludes files already in subdirectories


Process Each CSV File

Generates a timestamp (format: YYYYMMDD-HHMMSS)
Creates new filename: originalname-YYYYMMDD-HHMMSS.csv
Logs the operation and file contents to organizer.log
Moves file to archive/ with new name



Example Workflow
Before Running Script
project/
├── grade-generator.py
├── grades.csv
└── organizer.sh
After Running Script
project/
├── archive/
│   └── grades-20251105-170130.csv
├── grade-generator.py
├── organizer.log
└── organizer.sh
Multiple Runs
If you run the script again with new CSV files:
project/
├── archive/
│   ├── grades-20251105-170130.csv
│   └── grades-20251105-180245.csv
├── grade-generator.py
├── organizer.log    # Accumulates entries from both runs
└── organizer.sh
Log File Format
The organizer.log file contains detailed information about each archival operation:
==========================================
Archive Action - 2025-11-05 17:01:30
==========================================
Original File: grades.csv
New Location: archive/grades-20251105-170130.csv
Timestamp: 20251105-170130

File Contents:
------------------------------------------
Assignment,Category,Grade,Weight
Group Coding Lab,FA,85,30
Final Exam,SA,78,40
------------------------------------------
Archive completed successfully.
Script Features
Timestamp Format
Timestamps use the format YYYYMMDD-HHMMSS:

YYYY - Four-digit year (e.g., 2025)
MM - Two-digit month (01-12)
DD - Two-digit day (01-31)
HH - Two-digit hour in 24-hour format (00-23)
MM - Two-digit minute (00-59)
SS - Two-digit second (00-59)

Example: 20251105-170130 = November 5, 2025 at 5:01:30 PM
CSV File Organizer (organizer.sh)
A Bash shell script that automatically archives CSV files with timestamps and maintains a detailed log of all operations.
Overview
This script is part of the African Leadership University Individual Coding Lab for Introduction to Python Programming and Databases (BSE Year 1, Trimester 2). It works alongside the grade-generator.py script to organize and preserve CSV output files.
Purpose
The organizer script:

Archives all CSV files in the current directory
Adds timestamps to filenames for version tracking
Logs all operations including file contents
Maintains a cumulative log across multiple runs

Requirements

Bash shell (Linux, macOS, or Git Bash on Windows)
Read/write permissions in the current directory

Installation

Download organizer.sh to your working directory
Make the script executable:

bash   chmod +x organizer.sh
Usage
Basic Execution
bash./organizer.sh
What Happens

Check/Create Archive Directory

Checks if an archive/ directory exists
Creates it if not present


Find CSV Files

Searches for all .csv files in the current directory
Excludes files already in subdirectories


Process Each CSV File

Generates a timestamp (format: YYYYMMDD-HHMMSS)
Creates new filename: originalname-YYYYMMDD-HHMMSS.csv
Logs the operation and file contents to organizer.log
Moves file to archive/ with new name



Example Workflow
Before Running Script
project/
├── grade-generator.py
├── grades.csv
└── organizer.sh
After Running Script
project/
├── archive/
│   └── grades-20251105-170130.csv
├── grade-generator.py
├── organizer.log
└── organizer.sh
Multiple Runs
If you run the script again with new CSV files:
project/
├── archive/
│   ├── grades-20251105-170130.csv
│   └── grades-20251105-180245.csv
├── grade-generator.py
├── organizer.log    # Accumulates entries from both runs
└── organizer.sh
Log File Format
The organizer.log file contains detailed information about each archival operation:
==========================================
Archive Action - 2025-11-05 17:01:30
==========================================
Original File: grades.csv
New Location: archive/grades-20251105-170130.csv
Timestamp: 20251105-170130

File Contents:
------------------------------------------
Assignment,Category,Grade,Weight
Group Coding Lab,FA,85,30
Final Exam,SA,78,40
------------------------------------------
Archive completed successfully.
Script Features
Timestamp Format
Timestamps use the format YYYYMMDD-HHMMSS:

YYYY - Four-digit year (e.g., 2025)
MM - Two-digit month (01-12)
DD - Two-digit day (01-31)
HH - Two-digit hour in 24-hour format (00-23)
MM - Two-digit minute (00-59)
SS - Two-digit second (00-59)

Example: 20251105-170130 = November 5, 2025 at 5:01:30 PM