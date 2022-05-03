from st.student import Student


# 3

def get_modified_students(students):
    modified_students = []
    for student in students:
        flag = 0
        for grade in student.grades:
            if (grade == 3):
                flag += 1
        if (flag == 1):
            modified_students.append(student)

    return modified_students


students = Student.get_students('students.txt')

modified_students = get_modified_students(students)

for student in modified_students:
    print(str(student))
