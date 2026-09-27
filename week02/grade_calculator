students = []
while True:
    name = input("Enter student name or q to quit:")
    if name.lower() == "q":
        break
    score = int(input("Enter student score: "))
    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        continue
    elif score >= 90:
        grade = "A" 
    elif score >= 80:  
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    students.append((name, score, grade))

if len(students) > 0:
    print("Students Entered:", len(students))
    total = 0
    for name, score, grade in students:
        total += score
    average = total / len(students)
    print("Class Average:", average)
    for name, score, grade in students:
        print(name, "-", grade)
else:
    print("No students were entered.")



print("\nQuitting the program.")
