class Course:

    def __init__(self, name):
        self.name = name
        self.students = [] # Список студентов проходящих данный курс  best_student_1, best_student_2 т тд
        self.lectures = [] # Список lectures class Lecture 
        self.homeworkGrades = {} #class Student: int[] оценки студентов за домашнее задание 
        self.isFinished = False

    def GetAverageHomeworkGrade(self) -> float: #Проходиться в словаре  homeworkGrades и вычислять среднюю оценку студента в ключь добавляем сумму оценок, в значение добавлем колличетсво оценок. 
        sum = 0
        num = 0
        return sum / num

    def GetAverageLecturerRating(self) -> float: #Проходиться по списку лекций и считает средний рейтинг для каждого лектора
        pass

class Lecture:
    def __init__(self, lectureName, lecturer):
        self.lectureName = lectureName
        self.ratings = {} # class Student - Int
        self.lecturer = lecturer
    
    def __str__(self):
        return self.lectureName

    __repr__ = __str__

          

class School:
    def __init__(self):
        self.courses = [] # -courses[]: Course[]

class SchoolPerson:
    # firstName = ''
    # lastName = ''
    # school: School = None #School

    def __init__(self, firstName, lastName, school) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.school = school
    
    def __str__(self):
        return self.firstName + " " + self.lastName

    __repr__ = __str__

class Student(SchoolPerson):
    
    def RateLecturer(self, lecture ,rating:int): #lecturer: Lecturer, mark: Int
        if rating <= 10 and rating >= 0:
            lecture.ratings[self] = rating 
        else:
            print('Error')

    def GetAverageHomeworkGrade(self) -> float: 
        pass
    def __getCourses(self, isFinished) -> list: #isFinished: Bool # -> corses[]
        pass
    def GetCurrentCourses(self) -> list: # -> corses[]
        pass
    def GetFinishedCourses(self) -> list: # -> corses[]
        self.isFinished = True
        return
    def __cmp__(self, other):
        pass

class Mentor(SchoolPerson):
    pass

class Lecturer(Mentor):
    def GetAverageRating(self) -> float: 
        pass
    def __str__(self):
        pass
    def __cmp__(self, other):
        pass

class Reviewer(Mentor):
    def ReviewHomework(self, student, course) -> None: #student: Student, course: Course #
       pass

    def __str__(self):
        pass    

school = School()
intro_python_course = Course('Вводный модуль для студентов профессий PD и FPY')
python_course = Course('Python-разработчик с нуля')
git_course = Course('Git — система контроля версий')



# Список студентов
best_student_1 = Student('Иванов', 'Иван', school)
best_student_2 = Student('Мельникова', 'Ксения', school)
best_student_3 = Student('Ардаков', 'Игорь', school)
best_student_4 = Student('Донченко', 'Иван', school)
best_student_5 = Student('Кулагина', 'Юлия', school)
best_student_6 = Student('Бирюков', 'Евгений', school)
best_student_7 = Student('Васильев', 'Валерий', school)
best_student_8 = Student('Дылдин', 'Алексей', school)
best_student_9 = Student('Девин', 'Игорь', school)

# Список Лекторов
cool_lecturer_1 = Lecturer('Some', 'Buddy', school)
cool_lecturer_2 = Lecturer('Some1', 'Buddy1', school)
cool_lecturer_3 = Lecturer('Some2', 'Buddy2', school)
cool_lecturer_4 = Lecturer('Some3', 'Buddy3', school)


student_group = [best_student_1, best_student_2, best_student_3, best_student_4, best_student_5, best_student_6, best_student_7, best_student_8, best_student_9]
python_course.students.extend(student_group)
git_course.students.extend(student_group)
intro_python_course.students.extend(student_group)



# Список лекций 
    # Вводный модуль для студентов профессий PD и FPY
lecturePhytonOpen_1 = Lecture('Добро пожаловать на курсы', cool_lecturer_1) 
lecturePhytonOpen_2 = Lecture('Вводное занятие', cool_lecturer_1)  
lecturePhytonOpen_3 = Lecture('Дополнительные материалы', cool_lecturer_1) 
lecturePhytonOpen_4 = Lecture('Как мотивировать себя учиться?', cool_lecturer_1) 
lecturePhytonOpen_5 = Lecture('Обучение и карьера Python-разработчика', cool_lecturer_1) 
lecturePhytonOpen_6 = Lecture('Добро пожаловать в Центр развития карьеры', cool_lecturer_1) 
    # Python-разработчик с нуля 
        # 1. Знакомство с Python
lecturePhyton_1 = Lecture('Python. Знакомство с консолью', cool_lecturer_2)
lecturePhyton_2 = Lecture('Условные конструкции. Операции сравнения', cool_lecturer_2)
lecturePhyton_3 = Lecture('Введение в типы данных', cool_lecturer_2)
lecturePhyton_4 = Lecture('Циклы', cool_lecturer_2)
lecturePhyton_5 = Lecture('Коллекции данных. Словари. Множества.', cool_lecturer_2)
lecturePhyton_6 = Lecture('Функции - использование встроенных и создание собственных', cool_lecturer_2)
lecturePhyton_7 = Lecture('ООП: объекты и классы. Взаимодействие между ними', cool_lecturer_2)

lecturePhyton_8 = Lecture('ООП: наследование, инкапсуляция и полиморфизм', cool_lecturer_3)
        # 2. Работа с файловой системой в Python
lecturePhyton_9 = Lecture('Открытие и чтение файла, запись в файл', cool_lecturer_3)
lecturePhyton_10 = Lecture('Работа с разными форматами данных', cool_lecturer_3)
        # 3. Работа с внешним API
lecturePhyton_11 = Lecture('Работа с библиотекой requests, http запросы', cool_lecturer_3)
lecturePhyton_12 = Lecture('Работа с классами на примере API VK', cool_lecturer_3)
        # Курсовой проект
lecturePhyton_13 = Lecture('Защита курсового проекта PY', cool_lecturer_3)
    # Git — система контроля версий
lectureGIT_1 = Lecture('1. Знакомство с системой контроля версий Git', cool_lecturer_4)
lectureGIT_2 = Lecture('2. Работа с локальным репозиторием в Git', cool_lecturer_4)
lectureGIT_3 = Lecture('3. Работа с удаленным репозиторием через GitHub', cool_lecturer_4)
lectureGIT_4 = Lecture('4. Командная работа в Git и GitHub', cool_lecturer_4)
lectureGIT_5 = Lecture('5. Командная работа в Git и GitHub. Часть 2', cool_lecturer_4)

# закрепляем лекции за преподователями
intro_python_course_lectures = [lecturePhytonOpen_1, lecturePhytonOpen_2, lecturePhytonOpen_3, lecturePhytonOpen_4, lecturePhytonOpen_5, lecturePhytonOpen_6]
python_course_lectures = [lecturePhyton_1, lecturePhyton_2, lecturePhyton_3, lecturePhyton_4, lecturePhyton_5, lecturePhyton_6, lecturePhyton_7, lecturePhyton_9, lecturePhyton_9, lecturePhyton_10, lecturePhyton_11, lecturePhyton_12, lecturePhyton_13]
git_course_lectures = [lectureGIT_1, lectureGIT_2, lectureGIT_3, lectureGIT_4, lectureGIT_5]

# 
python_course.lectures.extend(python_course_lectures)
git_course.lectures.extend(git_course_lectures)
intro_python_course.lectures.extend(intro_python_course_lectures)

print(intro_python_course.lectures)
print(python_course.lectures)
print(git_course.lectures)

print(intro_python_course.students)

best_student_1.RateLecturer(lecturePhyton_1, 10)

print(lecturePhyton_1.ratings)



#Занести лекции в класс Course в список self.lectures










