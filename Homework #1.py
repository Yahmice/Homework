class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses:  
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def average (self):
        for key, sub_dict in self.grades.items():
            values = sub_dict.values()
            res = sum(values) / len(values)
        print(res)

    def __str__(self):
        res = f'Имя: {self.name}, Фамилия: {self.surname}, Средняя оценка за лекции: {self.average}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}, Фамилия: {self.surname}'
        return res
        
 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# 
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)
some_reviwer = Reviewer('Some', 'Body')
some_lecturer = Lecturer('Some', 'Body')

best_student = Student('Shinra', 'Tensei', 'male')
best_student.courses_in_progress += ['Python']
best_student.rate_lecturer(some_lecturer, 'Python', 9)
