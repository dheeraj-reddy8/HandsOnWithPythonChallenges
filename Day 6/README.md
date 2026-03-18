Problem Description:

This project analyzes a user’s daily transaction data and classifies each transaction into categories such as Normal, Large, High Risk, and Invalid. Based on transaction patterns, the system determines whether the overall activity is Low Risk, Moderate Risk, or High Risk.

Algorithm / Approach :

The program takes the registration number and extracts its last digit.

It calculates the length of the student’s name and adds it to the extracted digit.

The resulting value is checked against a Fibonacci sequence to determine the number of transactions (5 or 7).

Transaction amounts are collected and classified into categories: Normal, Large, High Risk, and Invalid.

List comprehension is used to filter valid transactions and compute the total transaction value.

Pattern detection is performed based on frequency, total spending, and number of high-risk transactions.

The final risk level is determined using conditional logic.

The program starts by taking the registration number and extracting its last digit. Then, it takes the student’s name and calculates its length. These two values are added to generate a personalized number. This number is checked against a Fibonacci sequence to decide whether the number of transactions should be 5 or 7. The program then accepts transaction amounts and classifies them into normal, large, high-risk, and invalid categories using conditions. Finally, it calculates the total value and applies pattern detection rules to determine the overall risk level.

Personalization Logic

In my program, I applied a personalization rule based on two inputs: the last digit of the registration number and the length of the student’s name.


I combined these two values to generate a number, which is then used to decide the number of transactions dynamically. Instead of using a fixed value, I introduced a Fibonacci-based logic. I generated Fibonacci numbers up to 50 and checked whether the calculated value belongs to that series.


If the value is present in the Fibonacci series, the number of transactions is set to 5, otherwise it is set to 7. This makes the program behavior different for each user.


This personalization ensures that the system is dynamic, unique, and not fixed, since different users will have different registration numbers and name lengths.


Example 1
•	Registration Number = AP24110011591
•	Last digit = 1
•	Name = KRISHNA
•	Length of name = 7
 Calculation:
1 + 7 = 8
Fibonacci series (up to 50):
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
 8 is present in the Fibonacci series 
So,  Number of transactions = 5


In this case, the number of transactions is 5 (based on Fibonacci logic). The transaction values entered are:
3000, 4000, 5000, 100, 200
First, each transaction is classified into categories:
•	Normal (≤500) → 100, 200
•	Large (501–2000) → none
•	High Risk (>2000) → 3000, 4000, 5000
•	Invalid (≤0) → none


These values are stored in a dictionary under their respective categories.


Next, only valid transactions (greater than 0) are considered. Since all values are positive, all transactions are valid. The total transaction value is calculated:
 Total = 3000 + 4000 + 5000 + 100 + 200 = 12300


The summary is stored as a tuple:
 (12300, 5)


After that, pattern detection is performed:
•	Frequent Transactions → 5 > 5 → False
•	Large Spending → 12300 > 5000 → True
•	High-Risk Transactions Count → 3 → True


Since there are 3 high-risk transactions, the system detects a suspicious pattern.


Finally, based on the conditions:
•	Suspicious pattern → High Risk


Final Output
•	Normal: [100, 200]
•	Large: []
•	High Risk: [3000, 4000, 5000]
•	Invalid: []
•	Total Transaction Value: 12300
•	Number of Transactions: 5
 Final Risk Level: High Risk


Example 2 :

• Registration Number = AP24110011473
• Last digit = 3
• Name = DHEERAJ REDDY
• Length of name = 13

Calculation:

3 + 13 = 16

Fibonacci series (up to 50):
0, 1, 1, 2, 3, 5, 8, 13, 21, 34

16 is NOT present in the Fibonacci series

So, Number of transactions = 7
Transactions entered:
100, 600, 2500, -10, 300, 7000, 1500

• Normal (≤500) → 100, 300
• Large (501–2000) → 600, 1500
• High Risk (>2000) → 2500, 7000
• Invalid (≤0) → -10

Valid Transactions

 100, 600, 2500, 300, 7000, 1500

Total Transaction Value

Total = 100 + 600 + 2500 + 300 + 7000 + 1500 = 12000

Summary (Tuple)

 (12000, 7)

Pattern Detection 

• Frequent Transactions → 7 > 5 → True
• Large Spending → 12000 > 5000 → True
• High-Risk Transactions Count → 2 → False

Final Decision 

 No suspicious pattern (high-risk < 3)
 But frequent OR large spending is True

 Final Risk Level = Moderate Risk

Final Output 

• Normal: [100, 300]
• Large: [600, 1500]
• High Risk: [2500, 7000]
• Invalid: [-10]

• Total Transaction Value: 12000
• Number of Transactions: 7

 Final Risk Level: Moderate Risk



 Reflection :

The key logic decision I made was to introduce a Fibonacci-based personalization rule to dynamically determine the number of transactions instead of using a fixed value. This ensures that each user gets a unique execution path. Additionally, I prioritized the high-risk transaction count when determining the final risk level, since it is a stronger indicator of suspicious activity compared to transaction frequency or total spending.

Concepts Used:

Lists

Loops (for)

Conditional Statements

List Comprehension

Dictionary (for categorization)

Tuple (for summary)


Conclusion :

This project demonstrates how programming logic can be used to simulate real-world fraud detection systems. It helped improve problem-solving skills, logical thinking, and the ability to structure programs effectively.