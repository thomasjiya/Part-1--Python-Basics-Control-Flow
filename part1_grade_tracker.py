# Task 1 — Data Parsing & Profile Cleaning

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# We will store all cleaned students here
cleaned_students = []

# Req 1: Loop through each messy student
for student in raw_students:

    # Clean the name — remove spaces and convert to Title Case
    clean_name = student["name"].strip().title()

    # Convert roll from string to integer
    clean_roll = int(student["roll"])

    # Split marks string into a list of integers
    marks_list = student["marks_str"].split(", ")
    clean_marks = [int(m) for m in marks_list]

    # Build the cleaned student dictionary
    cleaned = {
        "name":  clean_name,
        "roll":  clean_roll,
        "marks": clean_marks
    }

    # Add to our cleaned list
    cleaned_students.append(cleaned)

    # Req 2: Validate the name
    # Check every word contains only alphabetic characters
    words = clean_name.split()
    is_valid = all(word.isalpha() for word in words)

    if is_valid:
        validity = "✓ Valid name"
    else:
        validity = "✗ Invalid name"

    # Req 3: Print the formatted profile card
    print("================================")
    print(f"Student : {clean_name}   {validity}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("================================")
    print()

# Req 4: Find student with roll number 103
# and print their name in ALL CAPS and lowercase
for student in cleaned_students:
    if student["roll"] == 103:
        print(f"ALL CAPS   : {student['name'].upper()}")
        print(f"lowercase  : {student['name'].lower()}")

#--------------------------------------------------------------------------------------------------------
# Task 2 — Marks Analysis Using Loops

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# Part 1: Print each subject with grade
print(f"\nGrade Report for {student_name}")
print("=" * 40)

for i in range(len(subjects)):
    subject = subjects[i]
    mark    = marks[i]

    # Assign grade based on marks range
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subject:<12} | Marks: {mark:<5} | Grade: {grade}")

print("=" * 40)

# Part 2: Calculate total, average, highest,lowest

total = sum(marks)

# Average rounded to 2 decimal places
average = round(total / len(marks), 2)

# Highest scoring subject
highest_mark    = max(marks)
highest_index   = marks.index(highest_mark)
highest_subject = subjects[highest_index]

# Lowest scoring subject
lowest_mark    = min(marks)
lowest_index   = marks.index(lowest_mark)
lowest_subject = subjects[lowest_index]

print(f"\nTotal Marks   : {total}")
print(f"Average Marks : {average}")
print(f"Highest       : {highest_subject} ({highest_mark})")
print(f"Lowest        : {lowest_subject} ({lowest_mark})")

# Part 3: While loop — add new subjects
print("\n--- Add New Subjects ---")
print("Type 'done' as subject name to stop\n")

new_count = 0  # count how many valid subjects added

while True:

    # Ask for subject name
    subject_name = input("Enter subject name: ")

    # Stop loop if user types done
    if subject_name.lower() == "done":
        break

    # Ask for marks
    marks_input = input(f"Enter marks for {subject_name} (0-100): ")

    # Check if input is a valid number
    try:
        new_mark = int(marks_input)

        # Check if marks are in valid range
        if 0 <= new_mark <= 100:
            subjects.append(subject_name)
            marks.append(new_mark)
            new_count += 1
            print(f"✓ {subject_name} added successfully!\n")
        else:
            print(f"⚠ Warning: Marks must be between 0 and 100. '{new_mark}' not added.\n")

    except ValueError:
        print(f"⚠ Warning: '{marks_input}' is not a valid number. Entry not added.\n")

# After loop ends
print(f"\n{new_count} new subject(s) added.")

# Updated average across all subjects
updated_total   = sum(marks)
updated_average = round(updated_total / len(marks), 2)
print(f"Updated Average : {updated_average}")
print(f"All Subjects    : {subjects}")
print(f"All Marks       : {marks}")

#---------------------------------------------------------------------------------------------------------
# Task 2 — Marks Analysis Using Loops

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# Part 1: Print each subject with grade
print(f"\nGrade Report for {student_name}")
print("=" * 40)

for i in range(len(subjects)):
    subject = subjects[i]
    mark    = marks[i]

    # Assign grade based on marks range
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subject:<12} | Marks: {mark:<5} | Grade: {grade}")

print("=" * 40)

# Part 2: Calculate total, average, highest,lowest

total = sum(marks)

# Average rounded to 2 decimal places
average = round(total / len(marks), 2)

# Highest scoring subject
highest_mark    = max(marks)
highest_index   = marks.index(highest_mark)
highest_subject = subjects[highest_index]

# Lowest scoring subject
lowest_mark    = min(marks)
lowest_index   = marks.index(lowest_mark)
lowest_subject = subjects[lowest_index]

print(f"\nTotal Marks   : {total}")
print(f"Average Marks : {average}")
print(f"Highest       : {highest_subject} ({highest_mark})")
print(f"Lowest        : {lowest_subject} ({lowest_mark})")

# Part 3: While loop — add new subjects
print("\n--- Add New Subjects ---")
print("Type 'done' as subject name to stop\n")

new_count = 0  # count how many valid subjects added

while True:

    # Ask for subject name
    subject_name = input("Enter subject name: ")

    # Stop loop if user types done
    if subject_name.lower() == "done":
        break

    # Ask for marks
    marks_input = input(f"Enter marks for {subject_name} (0-100): ")

    # Check if input is a valid number
    try:
        new_mark = int(marks_input)

        # Check if marks are in valid range
        if 0 <= new_mark <= 100:
            subjects.append(subject_name)
            marks.append(new_mark)
            new_count += 1
            print(f"✓ {subject_name} added successfully!\n")
        else:
            print(f"⚠ Warning: Marks must be between 0 and 100. '{new_mark}' not added.\n")

    except ValueError:
        print(f"⚠ Warning: '{marks_input}' is not a valid number. Entry not added.\n")

# After loop ends
print(f"\n{new_count} new subject(s) added.")

# Updated average across all subjects
updated_total   = sum(marks)
updated_average = round(updated_total / len(marks), 2)
print(f"Updated Average : {updated_average}")
print(f"All Subjects    : {subjects}")
print(f"All Marks       : {marks}")
#---------------------------------------------------------------------------------------------------------
# Task 3 — Class Performance Summary

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# Part 1 & 2: Loop, compute, print table

print(f"\n{'Name':<18}| {'Average':^7} | {'Status'}")
print("-" * 40)

pass_count     = 0
fail_count     = 0
topper_name    = ""
topper_average = 0
all_averages   = []  


for name, marks in class_data:
    average = round(sum(marks) / len(marks), 2)
    all_averages.append(average)
    if average >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1
    if average > topper_average:
        topper_average = average
        topper_name    = name

    print(f"{name:<18}| {average:^7.2f} | {status}")

# Part 3: Print summary after the table

class_average = round(sum(all_averages) / len(all_averages), 2)

print("-" * 40)
print(f"\nStudents Passed : {pass_count}")
print(f"Students Failed : {fail_count}")
print(f"Class Topper    : {topper_name} ({topper_average})")
print(f"Class Average   : {class_average}")
#---------------------------------------------------------------------------------------------------------
