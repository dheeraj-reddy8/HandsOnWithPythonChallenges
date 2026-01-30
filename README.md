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



