import random
import math
import copy
import numpy as np
import pandas as pd

students = []

for i in range(12):
    students.append({
        "id": i + 1,
        "marks": random.randint(40, 100),
        "attendance": random.randint(60, 100),
        "scores": [random.randint(10, 30), random.randint(20, 50)]
    })

marks_set = set()
att_set = set()

for i in students:
    marks_set.add(i["marks"])
    att_set.add(i["attendance"])

print("Unique Marks:", marks_set)
print("Unique Attendance:", att_set)

shallow = copy.copy(students)
deep = copy.deepcopy(students)

roll = int(input("Enter roll number: "))
r = roll % 3

choice = input("Enter inc or dec: ")
value = int(input("Enter value: "))

for i in range(len(shallow)):
    if i % (r + 1) == 0:

        shallow[i]["marks"] = shallow[i]["marks"] + math.sqrt(shallow[i]["marks"])
        if shallow[i]["marks"] > 100:
            shallow[i]["marks"] = 100

        shallow[i]["scores"][0] += 2

        if choice == "inc":
            shallow[i]["attendance"] += value
        else:
            shallow[i]["attendance"] -= value

        if shallow[i]["attendance"] > 100:
            shallow[i]["attendance"] = 100
        if shallow[i]["attendance"] < 0:
            shallow[i]["attendance"] = 0


for i in range(len(deep)):
    if i % (r + 1) == 0:

        deep[i]["marks"] = deep[i]["marks"] + math.sqrt(deep[i]["marks"])
        if deep[i]["marks"] > 100:
            deep[i]["marks"] = 100

        deep[i]["scores"][0] += 2

        if choice == "inc":
            deep[i]["attendance"] += value
        else:
            deep[i]["attendance"] -= value

        if deep[i]["attendance"] > 100:
            deep[i]["attendance"] = 100
        if deep[i]["attendance"] < 0:
            deep[i]["attendance"] = 0


df1 = pd.DataFrame(students)
df2 = pd.DataFrame(shallow)
df3 = pd.DataFrame(deep)

print("\nORIGINAL")
print(df1)

print("\nSHALLOW")
print(df2)

print("\nDEEP")
print(df3)

orig = []
shallow_marks = []

for i in range(len(students)):
    orig.append(students[i]["marks"])
    shallow_marks.append(shallow[i]["marks"])

mean_orig = np.mean(orig)
mean_shallow = np.mean(shallow_marks)
std = np.std(shallow_marks)

manual_mean = sum(shallow_marks) / len(shallow_marks)

drift = abs(mean_orig - mean_shallow)

threshold = 6

if drift == 0:
    status = "Stable Data"
elif drift <= threshold:
    status = "Minor Drift"
elif drift <= 12:
    status = "Critical Drift"
else:
    status = "Copy Failure Detected"

result = (mean_shallow, drift, std)

print("\nDRIFT:", drift)
print("STD:", std)
print("MANUAL MEAN:", manual_mean)
print("TUPLE:", result)
print("STATUS:", status)

print("\nEXPLANATION:")
print("Shallow copy affects original because inner objects are shared.")
print("Deep copy does not affect original because it is independent.")