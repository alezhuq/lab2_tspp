from st.student import Student


# 5

def get_modified_students(students):
    modified_students = []

    for student in students:
        flag = True

        for i in student.grades:
            if i < 5:
                flag = False
                break

        if flag:
            modified_students.append(student)

    return modified_students


students = Student.get_students('students.txt')

modified_students = get_modified_students(students)

for student in modified_students:
    print(str(student))
