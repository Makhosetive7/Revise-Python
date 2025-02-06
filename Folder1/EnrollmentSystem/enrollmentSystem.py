# Original data
courses_data = {'informationTechnology': 4, 'foodScience': 3,
                'labTech': 3, 'EHT': 6, 'quantitySurvey': 8}

# Dictionary to store course status
course_status = {}

for course, value in courses_data.items():
    if value >= 80:
        course_status[course] = "Full"
    elif value >= 70:
        course_status[course] = "Full"
    elif value >= 60:
        course_status[course] = "Full"
    elif value >= 50:
        course_status[course] = "Full"
    elif value >= 40:
        course_status[course] = "Full"
    else:
        course_status[course] = "Not Full"

# Print each course status
for course, status in course_status.items():
    print(f"{course}: {status}")

# Print the highest and lowest score
highest_course = max(courses_data, key=courses_data.get)
lowest_course = min(courses_data, key=courses_data.get)

print(f"Highest: {highest_course} ({courses_data[highest_course]})")
print(f"Lowest: {lowest_course} ({courses_data[lowest_course]})")