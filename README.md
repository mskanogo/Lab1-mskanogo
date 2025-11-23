Grade Generator — Project Overview
The Grade Generator is a Python-based tool created for the Introduction to Python Programming and Databases course at African Leadership University (BSE Year 1, Trimester 2). Its purpose is to help students and instructors calculate final grades using weighted assignments across Formative (FA) and Summative (SA) categories.

The script guides users through entering multiple assignments, validates each input, computes final results, and exports everything into a clean CSV file—making grade tracking simple and reliable.

What the Script Does
Key Features
- User-friendly, interactive command-line interface
- Validates grades, categories (FA/SA), and weights
- Calculates weighted grades for each assignment
- Determines pass/fail based on performance in both categories
- Computes GPA on a 5.0 scale
- Displays a clear summary in the console
- Automatically exports all results into a grades.csv file
Requirements
- Python 3.x
- No external libraries needed (only the csv module)
How to Use It
Running the Program:
python grade-generator.py
Input Requirements:
- Assignment name
- Category (FA/SA)
- Grade (0–100)
- Weight (positive number)
Validation Rules:
- Grade must be between 0 and 100
- Category must be FA or SA
- Weight must be positive
- Grades and weights must be valid numbers
Calculation Logic:
Weighted Grade = (Grade / 100) × Weight
Totals: FA total, SA total, final grade, GPA
Pass/Fail:
A student must score at least 50% in both FA and SA categories to pass.
Outputs:
- Console summary
- CSV export (grades.csv)
File Structure:
grade-generator.py contains functions for validation, data collection, calculation, summary printing,
CSV export, and main program flow.
CSV File Organizer — organizer.sh
This script archives CSV files, adds timestamps, and logs all operations. It ensures all generated CSV
files are organized and preserved properly.
Usage:
chmod +x organizer.sh
./organizer.sh
Features:
- Creates archive folder if needed
- Finds all CSV files
- Adds timestamp (YYYYMMDD-HHMMSS)
- Moves files into archive/
- Logs operations in organizer.log
Log Example Included.