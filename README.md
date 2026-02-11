This project is a Python program that analyzes student marks and classifies their performance.
The program also includes a personalized bonus system based on the student’s name and registration number.

The main aim of this project is to use basic Python concepts like loops, lists, and conditions to build a simple grading system.

The objectives of this program are:

To take student details as input

To calculate a personalized value

To store student marks in a list

To apply bonus marks based on a condition

To classify students into grade categories

To count total valid and failed students

To display a final summary

Personalization Logic

The program uses personal details to create a special number.

Step 1: Length of Name

The length of the name is calculated using:

length = len(name)

Step 2: Last Two Digits of Registration Number

The last two digits are taken without using slicing:

num2 = int(reg[len(reg)-2])
num1 = int(reg[len(reg)-1])
last = num2 * 10 + num1

Step 3: Special Value

The personalized value is calculated as:

cal = length + last


This value is used to check the bonus condition.

Bonus Condition:

For each student mark, the program checks:

(mark % cal == 0) OR (cal % mark == 0)


If at least one student satisfies this condition:

5 bonus marks are added to all students

If marks become more than 100, they are set to 100

If no student satisfies the condition:

No bonus is applied

Grade Classification:

After applying bonus, marks are classified as:

90 to 100 → Excellent

75 to 89 → Very Good

60 to 74 → Good

40 to 59 → Average

0 to 39 → Fail

Less than 0 or more than 100 → Invalid

Counters Used:

Two counters are used:

valid → counts students with marks 40 and above

fail → counts students with marks below 40

At the end, the program prints:

Total Valid Students

Total Failed Students