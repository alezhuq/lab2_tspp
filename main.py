from st.student import Student


# 2.
def get_modified_students(students):
    result = []
    for student in students:
        flag = False
        flag2 = False
        flag3 = True
        for grade in student.grades:
            if grade == 5:
                flag = True
            if grade == 4:
                flag2 = True
            if grade <= 3:
                flag3 = False
        if flag and flag2 and flag3:
            result.append(student)

    return result


students = Student.get_students('students.txt')

modified_students = get_modified_students(students)

for student in modified_students:
    print(str(student))
