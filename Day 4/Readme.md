Personalized Risk Analyzer with Fibonacci-Based Personalization

Project Overview:

This Python program categorizes user-provided scores into Low, Medium, High, and Critical Risk groups. It then applies personalization based on the last digit of the student's registration number and a user-defined Fibonacci sequence. This ensures that each student's output is unique and tailored to their input.

Features:

Accepts registration number and a list of scores from the user.

Categorizes scores into risk levels:

Low Risk (0–30)

Medium Risk (31–60)

High Risk (61–100)

Critical Risk (>100)

Generates a Fibonacci sequence (<9) based on user input.

Allows users to select active Fibonacci numbers for personalization.

Applies personalization rules:

If the registration number’s last digit is in the active Fibonacci list → Low Risk scores removed.

If the last digit is not in the list → Critical Risk scores removed.

Displays risk categories before and after personalization.

Shows valid, ignored, and removed entries.

How to Use

Run the Python program.

Enter your registration number.

Enter the number of scores and input each score.

Enter the first two Fibonacci numbers (0 or 1) and the total number of Fibonacci numbers to generate (<9).

Choose which Fibonacci numbers to include in your active list (0 = exclude, 1 = include).

View the risk categorization before and after personalization along with summary counts.

Logic / Approach:

Scores are classified into risk categories using conditional statements.

A Fibonacci sequence is generated dynamically based on the user’s input using index-based calculation (no negative indexing or slicing).

Users select active Fibonacci numbers for personalization.

The program checks if the last digit of the registration number is in the active Fibonacci list:

Present → remove Low Risk entries.

Not present → remove Critical Risk entries.

Final outputs display updated risk categories and counts for valid, ignored, and removed entries.

Learning Outcomes:

Learned to categorize and analyze numerical data.

Gained experience in user input validation and handling.

Practiced generating dynamic Fibonacci sequences.

Applied personalization logic to produce individualized results.

Improved skills in list handling, indexing, and conditional programming.

Sample Output:

Enter Registration Number:AP24110011473
Registration Number last Digit: 3
Enter number  of scores :5
[0, 0, 0, 0, 0]
Enter Score:40
Enter Score:50
Enter Score:60
Enter Score:70
Enter Score:80
[40, 50, 60, 70, 80]
 Before Personalizing:
Low Risk: []
Median Risk: [40, 50, 60]
High Risk: [70, 80]
Critical Risk: []
Create a Finonacci list less than 9
Enter first fibonacci number 0 or 1: 1
Enter second fibonacci number 0 or 1: 1
Enter Fibonacci Number to generate less than 9:8
Your Fibonacci series: [1, 1, 2, 3, 5, 8]
Enter 0 or 1 to include each fibonacci number:
Include 1? (0/1): 1
Include 1? (0/1): 0
Include 2? (0/1): 1
Include 3? (0/1): 0
Include 5? (0/1): 1
Include 8? (0/1): 0
Your Active Fibonacci list: [1, 0, 2]
 After Personalizing:
Low Risk: []
Median Risk: [40, 50, 60]
High Risk: [70, 80]
Critical Risk: []
Total Valid Entries: 5
Total Ignored Entries: 0
Removed Entries after Personalization: 0




Total Valid Entries: 5
Total Ignored Entries: 1
Removed Entries after Personalization: 1
