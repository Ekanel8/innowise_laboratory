students = []

def add_student():
    name = input("Student name: ")
    for s in students:
        if s["name"] == name:
            print("Student already exists")
            return

    new_student = {"name": name, "grades": []}
    students.append(new_student)
    print("Student added")


def add_grades():
    name = input("Student name: ")

    for student in students:
        if student["name"] == name:
            while True:
                grade_input = input("Enter grade (0-100) or 'done' to finish: ")
                if grade_input.lower() == 'done':
                    break
                try:
                    grade = int(grade_input)
                    if 0 <= grade <= 100:
                        student["grades"].append(grade)
                    else:
                        print("Grade must be between 0 and 100")
                except ValueError:
                    print("Invalid input, enter a number")
            return

    print("Student not found")

def show_report():
    if not students:
        print("No students available")
        return

    averages = []

    for student in students:
        try:
            avg = sum(student["grades"]) / len(student["grades"])
            print(f"{student['name']}'s average grade is {avg:.1f}")
            averages.append(avg)
        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A")

    if averages:
        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = sum(averages) / len(averages)
        print("\n--- Overall Summary ---")
        print(f"Max average: {max_avg:.1f}")
        print(f"Min average: {min_avg:.1f}")
        print(f"Overall average: {overall_avg:.1f}")
    else:
        print("No grades available for summary")

def top_performer():
    students_with_grades = [s for s in students if s["grades"]]
    if not students_with_grades:
        print("No students with grades available")
        return

    top = max(
        students_with_grades,
        key=lambda s: sum(s["grades"]) / len(s["grades"])
    )
    avg = sum(top["grades"]) / len(top["grades"])
    print(f"Top performer: {top['name']} with average {avg:.1f}")


while True:
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Show report")
    print("4. Find top performer")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        add_grades()
    elif choice == 3:
        show_report()
    elif choice == 4:
        top_performer()
    elif choice == 5:
        break
    else:
        print("Wrong option")
