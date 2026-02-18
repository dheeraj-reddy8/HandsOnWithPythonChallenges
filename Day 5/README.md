Emergency Resource Dispatch Analyzer

Project Overview:

The Emergency Resource Dispatch Analyzer is a Python-based program designed to simulate how a disaster command center processes and analyzes resource requests from different zones.
The system classifies requests, handles invalid or unrealistic values, and applies a personalized filtering rule to generate a final dispatch plan.

Problem Statement:

During a disaster drill, different zones submit requests for resources. These requests may contain:

Invalid values

Unrealistic demands

Duplicate entries

Critical shortages

The command center must:

Accept a list of resource requests.

Classify each request based on its value.

Apply a personalized filtering rule using the PLI value.

Generate a final dispatch report.

Classification Rules:

Each request is categorized as follows:

Request Value	Category
< 0	            Invalid Request
0	            No Demand
1 – 20	        Low Demand
21 – 50	        Moderate Demand
> 50	        High Demand

The program stores results in the following lists:

1.low_demand

2.moderate_demand

3.high_demand

4.invalid_requests

Personalization Logic (PLI):

Personalization is based on the user’s name.

Steps

Calculate L = length of the name (excluding spaces).

Compute PLI = L % 3.

Personalization Rules
PLI Value	Rule Applied
0	        Remove all Low Demand requests
1	        Remove all High Demand requests
2	        Keep only Moderate Demand requests

Additional Features

The program also:

Counts total valid requests

Counts ignored (invalid) requests

Counts removed requests after personalization

Generates a Fibonacci sequence under 50

Uses Fibonacci values to control personalization activation

Displays final categorized lists

Program Workflow:

Accept number of requests from the user.

Store requests in a list.

Classify each request using a for loop.

Take user name and calculate PLI.

Generate a Fibonacci sequence.

Allow user to activate Fibonacci values.

Apply personalization rules.

Display final dispatch report.

Example Input
Requests: [10, 25, 60, -3, 0, 45, 80]
Name: Dheeraj Reddy

Example Output (Sample)
Length of name (no spaces (L)): 12
PLI Value: 0

Before Personalizing:
Low Demand: [10]
Moderate Demand: [25, 45]
High Demand: [60, 80]
Invalid Demand: [-3]

After Personalizing:
Low Demand: []
Moderate Demand: [25, 45]
High Demand: [60,800]
Invalid Demand: [-3]

Total Valid Entries: 6
Total Ignored Entries: 1
Removed Entries after Personalization: 1

Learning Outcomes:

Through this project, the following concepts were learned:

List creation and manipulation

For loop iteration

Conditional statements (if, elif, else)

Input handling

Counting and tracking values

Personalized logic implementation

Fibonacci sequence generation

Basic data analysis using Python

Technologies Used:

Python 

Basic console input/output


Core Python concepts (lists, loops, conditions)
