def calculate_grade(percentage):
    if percentage >= 60:
        return 'A'
    elif percentage >= 50:
        return 'B'
    elif percentage >= 40:
        return 'C'
    elif percentage >= 30:
        return 'D'
    else:
        return 'F'


name = input("Enter name: ")
roll = int(input("Enter roll number: "))

subjects = ["Maths", "Science", "English"]
marks = []

for subject in subjects:
    marks.append(int(input(f"Enter {subject} marks: ")))

total = sum(marks)
percentage = (total / 300) * 100
grade = calculate_grade(percentage)

print("\nResult")
print("Name:", name)
print("Roll number:", roll)

for i in range(len(subjects)):
    print(f"{subjects[i]} marks:", marks[i])

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
