def get_student_data():
    students = {}

    n = int(input("Enter the number of students: "))

    for i in range(n):
        name = input("Enter name: ")
        marks = list(map(int, input("Enter marks of 3 subjects: ").split()))
        students[name] = marks

    return students

def calculate_result(marks):
    total = sum(marks)
    avg = total/len(marks)

    if(avg >= 80):
        grade = "A"
    elif(avg >= 60):
        grade = "B"
    elif(avg >= 40):
        grade = "C"
    else:
        grade = "F"

    return total, avg, grade

def write_report(students):
    with open("student_report.txt", "w") as f:

        f.write("Student Report\n\n")

        for name, marks in students.items():
            total, avg, grade = calculate_result(marks)
            f.write(f"\nName : {name}")
            f.write(f"\nMark : {marks}")
            f.write(f"\nTotal : {total}")
            f.write(f"\nAverage : {avg}")
            f.write(f"\nGrade : {grade}\n")

data = get_student_data()
write_report(data)