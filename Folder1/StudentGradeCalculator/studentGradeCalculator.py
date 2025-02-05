
# Take 5 student names and their marks
studentNames = [{"Amanda": 20, "John": 35, "Nellie": 100, "Prince": 60, "Patience": 10}]

# Store them in a dictionary
studentGrades = {}

for student in studentNames[0]:
    if studentNames[0][student] >= 90:
        studentGrades[student] = "A"
    elif studentNames[0][student] >= 80:
        studentGrades[student] = "B"
    elif studentNames[0][student] >= 70:
        studentGrades[student] = "C"
    elif studentNames[0][student] >= 60:
        studentGrades[student] = "D"
    else:
        studentGrades[student] = "F"

# Print each student grade
for student, grade in studentGrades.items():
    print(f"{student}: {grade}")

# Print the highest and lowest score
highest = max(studentNames[0], key=studentNames[0].get)
lowest = min(studentNames[0], key=studentNames[0].get)

print(f"Highest: {highest} ({studentNames[0][highest]})")
print(f"Lowest: {lowest} ({studentNames[0][lowest]})")
