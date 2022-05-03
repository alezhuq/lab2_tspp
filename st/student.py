class Student:
    def __init__(self, name, birth_year, admission_year, grades):
        self.name = name 
        self.birth_year = birth_year
        self.admission_year = admission_year
        self.grades = [int(grade) for grade in grades]

    def __repr__(self):
        math, physics, english = self.grades
        return f'{self.name} - birth year: {self.birth_year}, year of admission: {self.admission_year}, math: {math}, physics: {physics}, english: {english}'

    @staticmethod
    def get_students(filepath):
        with open(filepath, 'r') as f:
            lines = f.read().splitlines()

            students = []

            for line in lines:
                info, grades = line.split(' ', 3), line.rsplit(' ', 3)
                info.pop()
                grades.pop(0)
                student = Student(*info, grades)
                students.append(student)
        return students