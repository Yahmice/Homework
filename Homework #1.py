
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    #Функция оценки лекторов
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:  
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    #Функция нахождения средней оценки у студента
    def avg(self):
        avg = []
        for value in self.grades.values():
            avg.extend(value)
        return sum(avg) / len(avg)

    #Функция вывода данных студента
    def __str__(self):
        res = f'Имя: {self.name}, Фамилия: {self.surname}, Средняя оценка за домашние задания: {self.avg()}, Курсы в процессе изучения: {self.courses_in_progress}, Завершенные курсы: {self.finished_courses}'
        return res

    #Функция для высчитывания средней оценки студента за курс
    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating  
    


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name, surname)
        self.grades = {}

    #Функция для высчитывания средней оценки лектора
    def average (self):
        for key, sub_dict in self.grades.items():
            res = sum(sub_dict) / len(sub_dict)
        return res

    #Функция сравнения
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer!')
            return
        return (self.average()) < (other.average())


    #Функция вывода данных о лекторе
    def __str__(self):
        res = f'Имя: {self.name}, Фамилия: {self.surname}, Средняя оценка за лекции: {self.average()}'
        return res
    
    #Функция для высчитывания средней оценки лектора за все его лекции в курсе
    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating  

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

#Практики
some_reviwer = Reviewer('Some', 'Body')
first_reviwer = Reviewer('Some', 'Body')

#Лекторы
some_lecturer = Lecturer('Some', 'One')
first_lecturer = Lecturer('Tim', 'Drake')


#Студенты
best_student = Student('Shinra', 'Tensei', 'male')
bad_student = Student('Dzundzi', 'Ito', 'male')


#Присоединение курсов
bad_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Python']

#Присоединение курсов к лекторам
first_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Python']

#Присоединение курсов к практикам
some_reviwer.courses_attached += ['Python']
first_reviwer.courses_attached += ['Python']



#Пройденные курсы 
best_student.finished_courses += ['Начало программирования']

#Оценки лекторов
best_student.rate_lecturer(some_lecturer, 'Python', 8)
bad_student.rate_lecturer(some_lecturer, 'Python', 4.6)

best_student.rate_lecturer(first_lecturer, 'Python', 6.7)
bad_student.rate_lecturer(first_lecturer, 'Python', 3)




#Оценки студентов
some_reviwer.rate_hw(best_student, 'Python', 9)
first_reviwer.rate_hw(best_student, 'Python', 8.7)

some_reviwer.rate_hw(bad_student, 'Python', 3)
first_reviwer.rate_hw(bad_student, 'Python', 2.5)

#Список студентов
student_list = [best_student, bad_student]
lecturer_list = [first_lecturer, some_lecturer]

#Функция для высчитывания средней оценки за курс
def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


#Проверка 4 - ого задания

# print(average_rating_for_course('Python', student_list))
# print(average_rating_for_course('Python', lecturer_list))


