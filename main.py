from st.student import Student


# 1

def get_modified_students(students):
    result = []
    for student in students:
        flag = True
        for grade in student.grades:
            if (grade != 5):
                flag = False
        if (flag):
            result.append(student)

    return result


students = Student.get_students('students.txt')

modified_students = get_modified_students(students)

for student in modified_students:
    print(str(student))
