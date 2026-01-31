CSE 205 Hands On With Python Daily Challenges:
This repository contains solutions for all daily challenges from the Hands-on Python (CSE205) – Code2Xplore 60 Days Challenge at SRM University-AP. Each day focuses on core Python concepts, problem-solving, and clean logic implementation under given constraints. All solutions are organized day-wise for easy reference.




Day-1 : Useer Profile Validation

This project is part of my Python Daily Challenges series.
On Day 1, I implemented a User Profile Verification system using basic Python concepts such as input handling, string validation, conditional statements, and boolean logic.

This program simulates real-world form validation used in registration systems.
The program accepts user details and verifies whether the entered information is valid based on specific rules.

Inputs Taken:
1.Full Name
2.Email ID
3.Mobile Number
4.Age
Each field is validated separately, and the final result determines whether the user profile is VALID or INVALID.

 What the Program Does:
Takes user inputs.
Validates Full Name, Email ID, Mobile Number, and Age.
Stores each validation result in a boolean variable.
Displays the final validation status.

Code Explanation:
The program starts by asking the user to enter their full name, email ID, mobile number, and age. Each input is checked separately to ensure it meets the required rules.
To validate the full name, the program checks three things. First, it ensures that the name contains at least two words by checking for a space. Second, it makes sure the name does not start with a space. Third, it checks that the name does not end with a space. If all these conditions are met, the variable Name_valid is set to true; otherwise, it is set to false.
For email validation, the program checks that the email contains both the at symbol and the dot. It also ensures that the at symbol is not the first character. If these rules are satisfied, the variable Email_valid is set to true; otherwise, it is set to false.
To validate the mobile number, the program checks that it has exactly 10 characters, that all characters are digits, and that the number does not start with 0. If all these conditions are met, the variable Mobile_valid is set to true; otherwise, it is set to false.
For age validation, the program checks whether the age is between 18 and 60. If it is, the variable Age_valid is set to true; otherwise, it is set to false.
Finally, the program checks all the validation results together. If Name_valid, Email_valid, Mobile_valid, and Age_valid are all true, the program prints "User Profile is VALID". If any one of them is false, it prints "User Profile is INVALID".

Day-2 : SmartId and Credential Validator

Student Credential Validation System Project Description This project implements a Student Credential Validation System using Python. The program verifies whether a student’s registration details satisfy predefined institutional rules and then decides whether the registration is APPROVED or REJECTED. The entire logic is implemented using string operations, indexing, and conditional statements only, without using loops, regular expressions, or advanced libraries. Inputs Required The program accepts the following inputs from the user: Student ID Email ID Password Referral Code Registration Number Registration Number Logic The Registration Number controls the order of validation. The last digit of the registration number is extracted. If the last digit is even, the program validates the Student ID first, followed by the Password. If the last digit is odd, the program validates the Password first, followed by the Student ID. This condition affects only the execution order, not the final result. For approval, all validations must be true. Example: AP24110011472 → Last digit is even → Student ID validated first AP24110011473 → Last digit is odd → Password validated first Validation Rules Student ID Validation Must contain exactly 7 characters Must follow the format CSE-XXX First three characters must be CSE Fourth character must be - Last three characters must be numeric digits Valid Example: CSE-245 Invalid Example: CSE245, CSE-12A Password Validation Must contain at least 7 characters First character must be an uppercase alphabet Must contain at least one numeric digit Valid Example: Aman1234 Invalid Example: amanabcd Email ID Validation Must contain both @ and . Should not start or end with @ Must end with .edu Valid Example: student@univ.edu Invalid Example: @univ.edu Referral Code Validation Must contain exactly 6 characters Must start with REF Characters at positions 4 and 5 must be digits Must end with @ Valid Example: REF45@ Invalid Example: REF4A@ Logic Used String indexing and slicing Character comparison Conditional statements (if, else) Boolean logic No loops, lists, dictionaries, or regular expressions are used in this program.


