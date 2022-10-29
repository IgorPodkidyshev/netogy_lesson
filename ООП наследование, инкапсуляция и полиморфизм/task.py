class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 

class Mentor:
    def __init__(self, name, surname, courses):
        self.name = name
        self.surname = surname
        self.courses = courses
        self.courses_attached = {}

    def __rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rear_score(self, student, course, grade):
        # 1 - проверяем существование студента в словаре у Student
        # 2- проверяем наличие курса у Lecturer
        # 3 - Добаляем к ключу Курса оценку (значнеие)

    


#Список студентов
best_student_1 = Student('Иванов', 'Иван')
best_student_2 = Student('Мельникова', 'Ксения')
best_student_3 = Student('Ардаков', 'Игорь', 'man')
best_student_4 = Student('Донченко', 'Иван', 'man')
best_student_5 = Student('Кулагина', 'Юлия', 'woman')
best_student_6 = Student('Бирюков', 'Евгений', 'man')
best_student_7 = Student('Васильев', 'Валерий', 'man')
best_student_8 = Student('Дылдин', 'Алексей', 'man')
best_student_9 = Student('Девин', 'Игорь', 'man')

#Список преподавалетей
best_student_1.courses_in_progress += ['Python']
best_student_1.courses_in_progress += ['Git']
cool_mentor = Mentor('Some', 'Buddy')
cool_lecturer = Lecturer('Some', 'Buddy')
cool_reviewer = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

best_student_1.name = input('Введите имя: ')

#Список команд для Студента
print(best_student_1.name)


# Список команд для Ментора

# Список команд для Лектора

# Список команд для Эксперта
    # Добавление ключа и оценки в словарь
def __rear_score(self, student, course, grade)



cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer._Mentor__rate_hw(best_student_1, 'Python', 10)
cool_reviewer._Mentor__rate_hw(best_student_1, 'Python', 8)
cool_reviewer._Mentor__rate_hw(best_student_1, 'Python', 9)

cool_reviewer._Mentor__rate_hw(best_student_1, 'Git', 10)
cool_reviewer._Mentor__rate_hw(best_student_1, 'Git', 7)
cool_reviewer._Mentor__rate_hw(best_student_1, 'Git', 8)
 
print(best_student_1.grades)

help = '''
s - Меню Студента
m - Меню Ментора
l - Меню Лектора
r - Меню Эксперта'''

# while True:
#     command = (str(input('Введите команду: ')))
#     if command == 's':
#         pass
#     elif command == 'm':
#         pass
#     elif command == 'l':
#         pass
#     elif command == 'r':
#         pass
#     elif command == 'help':
#         print(help)
