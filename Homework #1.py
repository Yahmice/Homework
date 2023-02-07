class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:  
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def avg(self):
        for key, values in self.grades.items():
            averaga = sum(values) / len(values)
        return averaga
    
    def __str__(self):
        res = f'Имя: {self.name}, Фамилия: {self.surname}, Средняя оценка за домашнее задание: {self.avg()}, Курсы в процессе изучения: {self.courses_in_progress}, Завершенные курсы: {self.finished_courses}'
        return res

    


    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name, surname)
        self.grades = {}

    def average (self):
        for key, sub_dict in self.grades.items():
            res = sum(sub_dict) / len(sub_dict)
        return res

    def __str__(self):
        res = f'Имя: {self.name}, Фамилия: {self.surname}, Средняя оценка за лекции: {self.average()}'
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
first_reviwer = Reviewer('Some', 'Body')
second_reviwer = Reviewer('Some', 'Body')
third_reviwer = Reviewer('Some', 'Body')
some_lecturer = Lecturer('Some', 'One')

#Студенты
best_student = Student('Shinra', 'Tensei', 'male')
middle_student = Student('Sakura', 'Uchiha', 'female')
bad_student = Student('Dzundzi', 'Ito', 'male')
average_student = Student('Ruoy', 'Eman', 'male')

#Присоединение курсов
average_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Python']
middle_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Python']
some_lecturer.courses_attached += ['Python']

#Пройденные курсы 
best_student.finished_courses += ['Начало программирования']

#Оценки лекторов
best_student.rate_lecturer(some_lecturer, 'Python', 8)
middle_student.rate_lecturer(some_lecturer, 'Python', 7.5)
average_student.rate_lecturer(some_lecturer, 'Python', 9)
bad_student.rate_lecturer(some_lecturer, 'Python', 4.6)

#Оценки студентов
some_reviwer.rate_hw(best_student, 'Python', 9)
first_reviwer.rate_hw(best_student, 'Python', 8.7)
second_reviwer.rate_hw(best_student, 'Python', 10)
third_reviwer.rate_hw(best_student, 'Python', 9.7)


print(best_student)

