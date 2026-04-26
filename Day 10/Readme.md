Academic Data Drift and Copy Behavior Analyzer

Project Overview
This project is based on analyzing student academic data in a university system. It studies how data changes when copied and modified using shallow copy and deep copy. The main aim is to understand data drift and how improper copying can affect original data in nested structures.

Objective
The objective of this project is to generate student data using random values, store it in a structured format, apply shallow and deep copy, modify the copied data, and analyze the changes using statistical methods. It helps in understanding data behavior, memory management, and data consistency in Python.

Data Format
Each student record contains id marks attendance and scores. Scores is a nested list containing internal and assignment marks. All records are stored in a list of dictionaries.

Features
Student data is generated using random values
Data is stored in list of dictionaries
Shallow copy and deep copy are created using copy module
Marks are updated using mathematical formula marks plus square root of marks
Attendance is modified based on user input increase or decrease
Nested score values are also modified
Values are restricted between zero and hundred to maintain validity

Statistical Analysis
Mean median and standard deviation are calculated using NumPy
One metric is calculated manually without using libraries
Data drift is calculated using difference between original and modified mean values
Based on drift value system behavior is classified as stable minor drift critical drift or copy failure

Key Concepts Used
Lists and dictionaries
Sets for unique value extraction
Functions
Random module
Math module
NumPy and Pandas
Shallow copy and deep copy
Data drift analysis

Important Rules
Marks and attendance values must not exceed 100
If values exceed 100 they are reset to 100
Only selected indexes are modified based on roll number rule

Conclusion
This project demonstrates how data copying methods affect original data. It shows that shallow copy can cause unintended changes due to shared references while deep copy maintains data independence and ensures safe data analysis.