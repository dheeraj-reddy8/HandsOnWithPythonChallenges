Student Credential Validation System
Project Description
This project implements a Student Credential Validation System using Python.
The program verifies whether a student’s registration details satisfy predefined institutional rules and then decides whether the registration is APPROVED or REJECTED.
The entire logic is implemented using string operations, indexing, and conditional statements only, without using loops, regular expressions, or advanced libraries.
Inputs Required
The program accepts the following inputs from the user:
Student ID
Email ID
Password
Referral Code
Registration Number
Registration Number Logic
The Registration Number controls the order of validation.
The last digit of the registration number is extracted.
If the last digit is even, the program validates the Student ID first, followed by the Password.
If the last digit is odd, the program validates the Password first, followed by the Student ID.
This condition affects only the execution order, not the final result.
For approval, all validations must be true.
Example:
AP24110011472 → Last digit is even → Student ID validated first
AP24110011473 → Last digit is odd → Password validated first
Validation Rules
Student ID Validation
Must contain exactly 7 characters
Must follow the format CSE-XXX
First three characters must be CSE
Fourth character must be -
Last three characters must be numeric digits
Valid Example: CSE-245
Invalid Example: CSE245, CSE-12A
Password Validation
Must contain at least 7 characters
First character must be an uppercase alphabet
Must contain at least one numeric digit
Valid Example: Aman1234
Invalid Example: amanabcd
Email ID Validation
Must contain both @ and .
Should not start or end with @
Must end with .edu
Valid Example: student@univ.edu
Invalid Example: @univ.edu
Referral Code Validation
Must contain exactly 6 characters
Must start with REF
Characters at positions 4 and 5 must be digits
Must end with @
Valid Example: REF45@
Invalid Example: REF4A@
Logic Used
String indexing and slicing
Character comparison
Conditional statements (if, else)
Boolean logic
No loops, lists, dictionaries, or regular expressions are used in this program.