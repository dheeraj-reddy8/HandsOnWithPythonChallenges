Student Performance Analysis System
Project Description

This project is developed to analyze student performance using Python programming. It considers multiple factors such as marks, attendance, and assignment scores to evaluate students. The system uses structured data and statistical methods to provide meaningful insights.

Objective

The main objective of this project is to study and analyze student performance using different parameters. It helps in identifying weak students, average performers, and top performers based on defined conditions.

Data Structure

Each student record contains the following fields:
Student ID
Marks
Attendance Percentage
Assignment Score
Performance Index

All student records are stored in a list and then converted into a Pandas DataFrame for analysis.

Technologies Used

Python programming language
NumPy for numerical operations
Pandas for data handling
Matplotlib for visualization
random module for data generation
math module for calculations

Methodology
Data Generation

The program generates data for 10 students using random values.
Marks are generated between 0 and 100.
Attendance is generated between 0 and 100.
Assignment scores are generated between 0 and 50.

Performance Index Calculation

The performance index is calculated using the formula:

Performance Index = (marks × 0.6 + assignment × 0.4) × log(attendance + 1)

This formula gives importance to both academic performance and attendance.

Classification of Students

Students are classified into the following categories based on conditions:

If marks are less than 40 or attendance is less than 50, the student is categorized as At Risk.
If marks are between 40 and 70, the student is categorized as Average.
If marks are between 71 and 90, the student is categorized as Good.
If marks are greater than 90 and attendance is greater than 80, the student is categorized as Top Performer.

Statistical Analysis

The program performs the following statistical operations:
Calculation of mean using NumPy
Calculation of median
Calculation of standard deviation
Manual calculation of mean without using built-in functions
Finding correlation between marks and attendance
Normalization of marks using formula

Normalized value = (x − minimum) ÷ (maximum − minimum)

Pattern Detection

Consistency is checked using standard deviation. If it is less than 15, the system is considered consistent.
Attendance risk is detected if more than 3 students have attendance below 50 percent.
High achievement is detected if at least 2 students are classified as top performers.

Final Insight

Based on the analysis, the system provides one of the following results:

Stable Academic System
Moderate Performance
Critical Attention Required

Visualization

A histogram is plotted to show the distribution of marks among the students. This helps in understanding how marks are spread across different ranges.

Input

The user is required to enter the last digit of the roll number.
If the entered value is not between 0 and 9, the program displays an error message.
If the input is 0, it is considered as 10 students.

Output

The program displays the following results:
Filtered student data in tabular form
Classification of students into categories
Statistical summary including mean, median, and standard deviation
Tuple containing mean, standard deviation, and maximum marks
Final system insight
Graph showing marks distribution

Conclusion

This project demonstrates how data analysis techniques can be applied to evaluate student performance. It highlights the use of Python libraries such as NumPy and Pandas for efficient computation and Matplotlib for visualization.