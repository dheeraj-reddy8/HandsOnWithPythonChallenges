Smart Inventory Mutation Tracker

Project Overview
This project simulates a warehouse inventory system where product data is stored with nested structures. It is designed to study how shallow copy and deep copy behave when data is modified, and how this leads to data drift or data integrity issues.

Problem Statement
The system maintains inventory data as a list of dictionaries. Each product contains item details such as price, stock, and nested supplier information. The program creates both shallow copy and deep copy of the inventory, applies controlled modifications, and compares results to analyze data behavior.

Data Format
Each inventory record contains item name, details such as price and stock, and supplier information such as name and rating. The supplier rating is added as an extra nested field to satisfy the test case requirement.

Custom Mutation Rule
The program uses the roll number to control modifications. Only the item at index calculated using roll number modulo length of inventory is selected for updates. This ensures that changes are applied to a specific position instead of the entire dataset.

Processing Logic
The system applies a discount by reducing price by ten percent and updates stock based on user input. These changes are applied only to the selected item. Both shallow copy and deep copy versions are modified separately to observe behavior differences.

Copy Behavior Analysis
Shallow copy fails to isolate changes because it copies only the outer structure while inner nested objects remain shared between original and copied data. As a result, modifications in nested fields such as price or stock reflect in the original data. Deep copy successfully avoids this issue because it creates a completely independent copy of all nested objects, ensuring that changes do not affect the original dataset. This behavior is verified through output comparison between original, shallow, and deep copy results.

Restriction Compliance
The program does not rely on predefined external explanations. Instead, the behavior of shallow and deep copy is demonstrated through actual program output and comparison of data structures.

Test Case Requirement
An additional nested field called supplier rating is included inside the supplier dictionary. This enhances the data structure and ensures compliance with the requirement of having at least one extra nested attribute.

Conclusion
This project demonstrates how improper copying can lead to unintended changes in original data. It clearly shows that shallow copy shares memory references for nested objects, while deep copy maintains full data independence. This helps in understanding safe data handling practices in real world systems.