class Course:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.students = [] # Список студентов проходящих данный курс  best_student_1, best_student_2 т тд
        self.lectures = [] # Список lectures class Lecture 
        self.homeworkGrades = {} #class Student: int[] оценки студентов за домашнее задание 
        self.lectionsGrades = {}
        self.isFinished = False
        self.school.courses.append(self)
    def GetAverageHomeworkGrade(self) -> float: #Законченно, черт его возьми! #Проходиться в словаре  homeworkGrades и вычислять среднюю оценку студента в ключь добавляем сумму оценок, в значение добавлем колличетсво оценок. 
        averagerating = {} #course: int[]
        course = []
        for grades in self.homeworkGrades.values():
            summa_step_1 = sum(grades)
            signs_step_1 = len(grades)
            course.append(summa_step_1/signs_step_1)
            summa_step_2 = sum(course)
            signs_step_2 = len(course)
            fin_result = summa_step_2/signs_step_2
            fixed = round(fin_result, 2)
            averagerating[self.name] = fixed    
        print(f'Средняя оценка у студентов за курс {self.name}: {averagerating[self.name]}')
            
    def GetAverageLecturerRating(self) -> float: #Законченно, черт его возьми! #Проходиться по списку лекций и считает средний рейтинг для каждого лектора
        lecturers = {}
        for lecture in self.lectures:
            if lecture.lecturer not in lecturers:
                lecturers[lecture.lecturer] = []
            lecturers[lecture.lecturer].extend(lecture.ratings.values())

        for lecturer, ratings in lecturers.items():
            if len(ratings) > 0: 
                averagerating = sum(ratings) / len(ratings)
                fixed = round(averagerating, 2)
                print(lecturer, fixed) 
    
    def __str__(self):
        return self.name

    __repr__ = __str__

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
    
    def __init__(self, firstName, lastName, school) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.school = school
        self.averagerating = {}
           
    def __str__(self):
        return self.firstName + " " + self.lastName 

    __repr__ = __str__

class Student(SchoolPerson):
    
    def RateLecturer(self, lecture ,rating:int): 
        if rating <= 10 and rating >= 0:
            lecture.ratings[self] = rating 
        else:
            print('Error')

    def GetAverageHomeworkGrade(self) -> float: 
        for course in self.school.courses:
            if self in course.students:
                if self in course.homeworkGrades and len(course.homeworkGrades[self]) > 0:
                    average_grade = sum(course.homeworkGrades[self]) / len(course.homeworkGrades[self])
                    fixed = round(average_grade, 2) 
                    return fixed      

    def __getCourses(self, isFinished) -> list: 
        courses = []
        for course in self.school.courses: 
            if self in course.students and course.isFinished == isFinished:
                courses.append(course)
        return courses         

    def GetCurrentCourses(self) -> list: # -> corses[] показывает на какие курсы ходит студент
        return self.__getCourses(False)
    def GetFinishedCourses(self) -> list: # -> corses[]
        return self.__getCourses(True)
    def __str__(self):
        return f'Фамилия: {self.firstName}\nИмя:{self.lastName}\nСредняя оценка за домашние задания:{self.GetAverageHomeworkGrade()}\nКурсы в процессе изучения:{self.GetCurrentCourses()}\nЗавершенные курсы:{self.GetFinishedCourses()} '

    __repr__ = __str__

    def __cmp__(self, other):
        return
        
    def __lt__ (self, other):
        return

class Mentor(SchoolPerson):
    pass

class Lecturer(Mentor):
    def __init__(self, firstName, lastName, school) -> None:
        super().__init__(firstName, lastName, school)
        
    def GetAverageRating(self) -> float: 
        ratings = []
        for course in self.school.courses:
            for lecture in course.lectures:
                if self == lecture.lecturer:
                    ratings.extend(lecture.ratings.values())
        if len(ratings) > 0:
            averagerating = sum(ratings) / len(ratings)
            fixed = round(averagerating, 2)
            return fixed
        else:
            return 'Нет оценок'
    def __str__(self):
        return f'Фамилия: {self.firstName}\nИмя:{self.lastName}\nСредняя оценка за лекции: {self.GetAverageRating()}'
    def __cmp__(self, other):
        pass
    def __lt__(self, other):
        return

class Reviewer(Mentor):
    def ReviewHomework(self, course, student, grade:int) -> None: #student: Student, course: Course #
        if grade <= 10 or grade >= 0:
            if not student in course.homeworkGrades:
                course.homeworkGrades[student] = []
            course.homeworkGrades[student].append(grade)
        else:
            print('Error')

    def __str__(self):
        return f'Фамилия: {self.firstName}\nИмя:{self.lastName}'    

school = School()
intro_python_course = Course('Вводный модуль для студентов профессий PD и FPY', school)
python_course = Course('Python-разработчик с нуля',school)
git_course = Course('Git — система контроля версий', school)

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
all_best_student = [best_student_1, best_student_2, best_student_3, best_student_4, best_student_5, best_student_6, best_student_7, best_student_8, best_student_9]
# Список Лекторов
cool_lecturer_1 = Lecturer('Some', 'Buddy', school)
cool_lecturer_2 = Lecturer('Some1', 'Buddy1', school)
cool_lecturer_3 = Lecturer('Some2', 'Buddy2', school)
cool_lecturer_4 = Lecturer('Some3', 'Buddy3', school)
all_cool_lectorers = [cool_lecturer_1, cool_lecturer_2, cool_lecturer_3, cool_lecturer_4]

#Список проверяющих
best_reviewer = Reviewer('Best', 'Reviewer', school)

student_intro_python_group = [best_student_1, best_student_2, best_student_3, best_student_4, best_student_5, best_student_6, best_student_7, best_student_8, best_student_9]
student_python_group = [best_student_1, best_student_2, best_student_3, best_student_4, best_student_5, best_student_6, best_student_7, best_student_8, best_student_9]
student_git_group = [best_student_1, best_student_2, best_student_3, best_student_4, best_student_5, best_student_6, best_student_7, best_student_8, best_student_9]

python_course.students.extend(student_python_group)
git_course.students.extend(student_git_group)
intro_python_course.students.extend(student_intro_python_group)

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
lecturePhyton_7 = Lecture('ООП: объекты и классы. Взаимодействие между ними', cool_lecturer_3)

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

# print(intro_python_course.lectures)
# print(python_course.lectures)
# print(git_course.lectures)

# print(intro_python_course.students)
# print(python_course.students)
# print(git_course.students)

# Добавляем оценки студентам
def enter_Grades():
# Вводный модуль для студентов профессий PD и FPY
    best_reviewer.ReviewHomework(intro_python_course, best_student_1, 10)
    best_reviewer.ReviewHomework(intro_python_course, best_student_1, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_1, 10)
    best_reviewer.ReviewHomework(intro_python_course, best_student_1, 8)
    best_reviewer.ReviewHomework(intro_python_course, best_student_1, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_1, 7)

    best_reviewer.ReviewHomework(intro_python_course, best_student_2, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_2, 10)
    best_reviewer.ReviewHomework(intro_python_course, best_student_2, 7)
    best_reviewer.ReviewHomework(intro_python_course, best_student_2, 6)
    best_reviewer.ReviewHomework(intro_python_course, best_student_2, 8)
    best_reviewer.ReviewHomework(intro_python_course, best_student_2, 9)

    best_reviewer.ReviewHomework(intro_python_course, best_student_3, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_3, 10)
    best_reviewer.ReviewHomework(intro_python_course, best_student_3, 7)
    best_reviewer.ReviewHomework(intro_python_course, best_student_3, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_3, 8)
    best_reviewer.ReviewHomework(intro_python_course, best_student_3, 9)

    best_reviewer.ReviewHomework(intro_python_course, best_student_4, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_4, 10)
    best_reviewer.ReviewHomework(intro_python_course, best_student_4, 5)
    best_reviewer.ReviewHomework(intro_python_course, best_student_4, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_4, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_4, 9)

    best_reviewer.ReviewHomework(intro_python_course, best_student_5, 10)
    best_reviewer.ReviewHomework(intro_python_course, best_student_5, 7)
    best_reviewer.ReviewHomework(intro_python_course, best_student_5, 5)
    best_reviewer.ReviewHomework(intro_python_course, best_student_5, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_5, 8)
    best_reviewer.ReviewHomework(intro_python_course, best_student_5, 9)

    best_reviewer.ReviewHomework(intro_python_course, best_student_6, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_6, 7)
    best_reviewer.ReviewHomework(intro_python_course, best_student_6, 5)
    best_reviewer.ReviewHomework(intro_python_course, best_student_6, 4)
    best_reviewer.ReviewHomework(intro_python_course, best_student_6, 8)
    best_reviewer.ReviewHomework(intro_python_course, best_student_6, 9)

    best_reviewer.ReviewHomework(intro_python_course, best_student_7, 2)
    best_reviewer.ReviewHomework(intro_python_course, best_student_7, 7)
    best_reviewer.ReviewHomework(intro_python_course, best_student_7, 5)
    best_reviewer.ReviewHomework(intro_python_course, best_student_7, 3)
    best_reviewer.ReviewHomework(intro_python_course, best_student_7, 8)
    best_reviewer.ReviewHomework(intro_python_course, best_student_7, 9)

    best_reviewer.ReviewHomework(intro_python_course, best_student_8, 6)
    best_reviewer.ReviewHomework(intro_python_course, best_student_8, 7)
    best_reviewer.ReviewHomework(intro_python_course, best_student_8, 8)
    best_reviewer.ReviewHomework(intro_python_course, best_student_8, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_8, 8)
    best_reviewer.ReviewHomework(intro_python_course, best_student_8, 9)

    best_reviewer.ReviewHomework(intro_python_course, best_student_9, 10)
    best_reviewer.ReviewHomework(intro_python_course, best_student_9, 7)
    best_reviewer.ReviewHomework(intro_python_course, best_student_9, 8)
    best_reviewer.ReviewHomework(intro_python_course, best_student_9, 9)
    best_reviewer.ReviewHomework(intro_python_course, best_student_9, 8)
    best_reviewer.ReviewHomework(intro_python_course, best_student_9, 10)

    intro_python_course.isFinished = True
    # GIT
    best_reviewer.ReviewHomework(git_course, best_student_1, 10)
    best_reviewer.ReviewHomework(git_course, best_student_1, 9)
    best_reviewer.ReviewHomework(git_course, best_student_1, 10)
    best_reviewer.ReviewHomework(git_course, best_student_1, 8)
    best_reviewer.ReviewHomework(git_course, best_student_1, 9)

    best_reviewer.ReviewHomework(git_course, best_student_2, 9)
    best_reviewer.ReviewHomework(git_course, best_student_2, 10)
    best_reviewer.ReviewHomework(git_course, best_student_2, 7)
    best_reviewer.ReviewHomework(git_course, best_student_2, 6)
    best_reviewer.ReviewHomework(git_course, best_student_2, 8)

    best_reviewer.ReviewHomework(git_course, best_student_3, 9)
    best_reviewer.ReviewHomework(git_course, best_student_3, 10)
    best_reviewer.ReviewHomework(git_course, best_student_3, 7)
    best_reviewer.ReviewHomework(git_course, best_student_3, 9)
    best_reviewer.ReviewHomework(git_course, best_student_3, 8)


    best_reviewer.ReviewHomework(git_course, best_student_4, 9)
    best_reviewer.ReviewHomework(git_course, best_student_4, 10)
    best_reviewer.ReviewHomework(git_course, best_student_4, 5)
    best_reviewer.ReviewHomework(git_course, best_student_4, 9)
    best_reviewer.ReviewHomework(git_course, best_student_4, 9)

    best_reviewer.ReviewHomework(git_course, best_student_5, 10)
    best_reviewer.ReviewHomework(git_course, best_student_5, 7)
    best_reviewer.ReviewHomework(git_course, best_student_5, 5)
    best_reviewer.ReviewHomework(git_course, best_student_5, 9)
    best_reviewer.ReviewHomework(git_course, best_student_5, 8)

    best_reviewer.ReviewHomework(git_course, best_student_6, 9)
    best_reviewer.ReviewHomework(git_course, best_student_6, 7)
    best_reviewer.ReviewHomework(git_course, best_student_6, 5)
    best_reviewer.ReviewHomework(git_course, best_student_6, 4)
    best_reviewer.ReviewHomework(git_course, best_student_6, 8)

    best_reviewer.ReviewHomework(git_course, best_student_7, 2)
    best_reviewer.ReviewHomework(git_course, best_student_7, 7)
    best_reviewer.ReviewHomework(git_course, best_student_7, 5)
    best_reviewer.ReviewHomework(git_course, best_student_7, 3)
    best_reviewer.ReviewHomework(git_course, best_student_7, 8)

    best_reviewer.ReviewHomework(git_course, best_student_8, 6)
    best_reviewer.ReviewHomework(git_course, best_student_8, 7)
    best_reviewer.ReviewHomework(git_course, best_student_8, 8)
    best_reviewer.ReviewHomework(git_course, best_student_8, 9)
    
    best_reviewer.ReviewHomework(git_course, best_student_9, 10)
    best_reviewer.ReviewHomework(git_course, best_student_9, 7)
    best_reviewer.ReviewHomework(git_course, best_student_9, 8)
    

    # python

    best_reviewer.ReviewHomework(python_course, best_student_1, 10)
    best_reviewer.ReviewHomework(python_course, best_student_1, 9)
    best_reviewer.ReviewHomework(python_course, best_student_1, 10)
    best_reviewer.ReviewHomework(python_course, best_student_1, 8)
    best_reviewer.ReviewHomework(python_course, best_student_1, 9)
    best_reviewer.ReviewHomework(python_course, best_student_1, 7)
    best_reviewer.ReviewHomework(python_course, best_student_1, 8)
    best_reviewer.ReviewHomework(python_course, best_student_1, 9)

    best_reviewer.ReviewHomework(python_course, best_student_2, 9)
    best_reviewer.ReviewHomework(python_course, best_student_2, 10)
    best_reviewer.ReviewHomework(python_course, best_student_2, 7)
    best_reviewer.ReviewHomework(python_course, best_student_2, 6)
    best_reviewer.ReviewHomework(python_course, best_student_2, 8)
    best_reviewer.ReviewHomework(python_course, best_student_2, 9)
    best_reviewer.ReviewHomework(python_course, best_student_2, 9)
    best_reviewer.ReviewHomework(python_course, best_student_2, 10)

    best_reviewer.ReviewHomework(python_course, best_student_3, 9)
    best_reviewer.ReviewHomework(python_course, best_student_3, 10)
    best_reviewer.ReviewHomework(python_course, best_student_3, 7)
    best_reviewer.ReviewHomework(python_course, best_student_3, 9)
    best_reviewer.ReviewHomework(python_course, best_student_3, 8)
    best_reviewer.ReviewHomework(python_course, best_student_3, 9)
    best_reviewer.ReviewHomework(python_course, best_student_3, 9)
    best_reviewer.ReviewHomework(python_course, best_student_3, 9)

    best_reviewer.ReviewHomework(python_course, best_student_4, 9)
    best_reviewer.ReviewHomework(python_course, best_student_4, 10)
    best_reviewer.ReviewHomework(python_course, best_student_4, 5)
    best_reviewer.ReviewHomework(python_course, best_student_4, 9)
    best_reviewer.ReviewHomework(python_course, best_student_4, 9)
    best_reviewer.ReviewHomework(python_course, best_student_4, 9)
    best_reviewer.ReviewHomework(python_course, best_student_4, 9)

    best_reviewer.ReviewHomework(python_course, best_student_5, 10)
    best_reviewer.ReviewHomework(python_course, best_student_5, 7)
    best_reviewer.ReviewHomework(python_course, best_student_5, 5)
    best_reviewer.ReviewHomework(python_course, best_student_5, 9)
    best_reviewer.ReviewHomework(python_course, best_student_5, 8)
    best_reviewer.ReviewHomework(python_course, best_student_5, 9)
    best_reviewer.ReviewHomework(python_course, best_student_3, 9)
    best_reviewer.ReviewHomework(python_course, best_student_3, 9)
    best_reviewer.ReviewHomework(python_course, best_student_3, 9)

    best_reviewer.ReviewHomework(python_course, best_student_6, 9)
    best_reviewer.ReviewHomework(python_course, best_student_6, 7)
    best_reviewer.ReviewHomework(python_course, best_student_6, 5)
    best_reviewer.ReviewHomework(python_course, best_student_6, 4)
    best_reviewer.ReviewHomework(python_course, best_student_6, 8)
    best_reviewer.ReviewHomework(python_course, best_student_6, 9)
    best_reviewer.ReviewHomework(python_course, best_student_6, 9)
    best_reviewer.ReviewHomework(python_course, best_student_6, 9)

    best_reviewer.ReviewHomework(python_course, best_student_7, 2)
    best_reviewer.ReviewHomework(python_course, best_student_7, 7)
    best_reviewer.ReviewHomework(python_course, best_student_7, 5)
    best_reviewer.ReviewHomework(python_course, best_student_7, 3)
    best_reviewer.ReviewHomework(python_course, best_student_7, 8)
    best_reviewer.ReviewHomework(python_course, best_student_7, 9)
    best_reviewer.ReviewHomework(python_course, best_student_7, 9)
    best_reviewer.ReviewHomework(python_course, best_student_7, 9)

    best_reviewer.ReviewHomework(python_course, best_student_8, 6)
    best_reviewer.ReviewHomework(python_course, best_student_8, 7)
    best_reviewer.ReviewHomework(python_course, best_student_8, 8)
    best_reviewer.ReviewHomework(python_course, best_student_8, 9)
    best_reviewer.ReviewHomework(python_course, best_student_8, 8)
    best_reviewer.ReviewHomework(python_course, best_student_8, 9)
    best_reviewer.ReviewHomework(python_course, best_student_8, 9)
    best_reviewer.ReviewHomework(python_course, best_student_8, 9)

    best_reviewer.ReviewHomework(python_course, best_student_9, 10)
    best_reviewer.ReviewHomework(python_course, best_student_9, 7)
    best_reviewer.ReviewHomework(python_course, best_student_9, 8)
    best_reviewer.ReviewHomework(python_course, best_student_9, 9)
    best_reviewer.ReviewHomework(python_course, best_student_9, 8)
    best_reviewer.ReviewHomework(python_course, best_student_9, 10)
    best_reviewer.ReviewHomework(python_course, best_student_9, 10)
    best_reviewer.ReviewHomework(python_course, best_student_9, 10)
enter_Grades()

# Выставляем оценку Лектору
def enter_Grades_lections():
    # Блок Питон
    # Лекция 1
    best_student_1.RateLecturer(lecturePhyton_1, 10)
    best_student_2.RateLecturer(lecturePhyton_1, 10)
    best_student_3.RateLecturer(lecturePhyton_1, 10)
    best_student_4.RateLecturer(lecturePhyton_1, 9)
    best_student_5.RateLecturer(lecturePhyton_1, 10)
    best_student_6.RateLecturer(lecturePhyton_1, 8)
    best_student_7.RateLecturer(lecturePhyton_1, 10)
    best_student_8.RateLecturer(lecturePhyton_1, 10)
    best_student_9.RateLecturer(lecturePhyton_1, 7)
    # Лекция 2
    best_student_1.RateLecturer(lecturePhyton_2, 10)
    best_student_2.RateLecturer(lecturePhyton_2, 10)
    best_student_3.RateLecturer(lecturePhyton_2, 10)
    best_student_4.RateLecturer(lecturePhyton_2, 10)
    best_student_5.RateLecturer(lecturePhyton_2, 1)
    best_student_6.RateLecturer(lecturePhyton_2, 10)
    best_student_7.RateLecturer(lecturePhyton_2, 6)
    best_student_8.RateLecturer(lecturePhyton_2, 8)
    best_student_9.RateLecturer(lecturePhyton_2, 9)
    # Лекция 3
    best_student_1.RateLecturer(lecturePhyton_3, 10)
    best_student_2.RateLecturer(lecturePhyton_3, 9)
    best_student_3.RateLecturer(lecturePhyton_3, 7)
    best_student_4.RateLecturer(lecturePhyton_3, 10)
    best_student_5.RateLecturer(lecturePhyton_3, 1)
    best_student_6.RateLecturer(lecturePhyton_3, 10)
    best_student_7.RateLecturer(lecturePhyton_3, 6)
    best_student_8.RateLecturer(lecturePhyton_3, 5)
    best_student_9.RateLecturer(lecturePhyton_3, 9)
    # Лекция 4
    best_student_1.RateLecturer(lecturePhyton_4, 10)
    best_student_2.RateLecturer(lecturePhyton_4, 9)
    best_student_3.RateLecturer(lecturePhyton_4, 7)
    best_student_4.RateLecturer(lecturePhyton_4, 10)
    best_student_5.RateLecturer(lecturePhyton_4, 9)
    best_student_6.RateLecturer(lecturePhyton_4, 10)
    best_student_7.RateLecturer(lecturePhyton_4, 6)
    best_student_8.RateLecturer(lecturePhyton_4, 10)
    best_student_9.RateLecturer(lecturePhyton_4, 9)
    # Лекция 5
    best_student_1.RateLecturer(lecturePhyton_5, 10)
    best_student_2.RateLecturer(lecturePhyton_5, 9)
    best_student_3.RateLecturer(lecturePhyton_5, 8)
    best_student_4.RateLecturer(lecturePhyton_5, 9)
    best_student_5.RateLecturer(lecturePhyton_5, 9)
    best_student_6.RateLecturer(lecturePhyton_5, 10)
    best_student_7.RateLecturer(lecturePhyton_5, 6)
    best_student_8.RateLecturer(lecturePhyton_5, 10)
    best_student_9.RateLecturer(lecturePhyton_5, 9)
    # Лекция 6
    best_student_1.RateLecturer(lecturePhyton_6, 2)
    best_student_2.RateLecturer(lecturePhyton_6, 10)
    best_student_3.RateLecturer(lecturePhyton_6, 8)
    best_student_4.RateLecturer(lecturePhyton_6, 8)
    best_student_5.RateLecturer(lecturePhyton_6, 9)
    best_student_6.RateLecturer(lecturePhyton_6, 6)
    best_student_7.RateLecturer(lecturePhyton_6, 10)
    best_student_8.RateLecturer(lecturePhyton_6, 10)
    best_student_9.RateLecturer(lecturePhyton_6, 9)
    # Лекция 7
    best_student_1.RateLecturer(lecturePhyton_7, 9)
    best_student_2.RateLecturer(lecturePhyton_7, 10)
    best_student_3.RateLecturer(lecturePhyton_7, 8)
    best_student_4.RateLecturer(lecturePhyton_7, 10)
    best_student_5.RateLecturer(lecturePhyton_7, 9)
    best_student_6.RateLecturer(lecturePhyton_7, 7)
    best_student_7.RateLecturer(lecturePhyton_7, 6)
    best_student_8.RateLecturer(lecturePhyton_7, 10)
    best_student_9.RateLecturer(lecturePhyton_7, 9)
    # Лекция 8
    best_student_1.RateLecturer(lecturePhyton_8, 9)
    best_student_2.RateLecturer(lecturePhyton_8, 8)
    best_student_3.RateLecturer(lecturePhyton_8, 8)
    best_student_4.RateLecturer(lecturePhyton_8, 9)
    best_student_5.RateLecturer(lecturePhyton_8, 9)
    best_student_6.RateLecturer(lecturePhyton_8, 7)
    best_student_7.RateLecturer(lecturePhyton_8, 6)
    best_student_8.RateLecturer(lecturePhyton_8, 10)
    best_student_9.RateLecturer(lecturePhyton_8, 9)

    # Блок 2 введение в питон
    # Лекция 1
    best_student_1.RateLecturer(lecturePhytonOpen_1, 9)
    best_student_2.RateLecturer(lecturePhytonOpen_1, 10)
    best_student_3.RateLecturer(lecturePhytonOpen_1, 8)
    best_student_4.RateLecturer(lecturePhytonOpen_1, 9)
    best_student_5.RateLecturer(lecturePhytonOpen_1, 9)
    best_student_6.RateLecturer(lecturePhytonOpen_1, 8)
    best_student_7.RateLecturer(lecturePhytonOpen_1, 6)
    best_student_8.RateLecturer(lecturePhytonOpen_1, 10)
    best_student_9.RateLecturer(lecturePhytonOpen_1, 9)
    # Лекция 2
    best_student_1.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_2.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_3.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_4.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_5.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_6.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_7.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_8.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_9.RateLecturer(lecturePhytonOpen_2, 9)
    # Лекция 3
    best_student_1.RateLecturer(lecturePhytonOpen_2, 8)
    best_student_2.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_3.RateLecturer(lecturePhytonOpen_2, 8)
    best_student_4.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_5.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_6.RateLecturer(lecturePhytonOpen_2, 8)
    best_student_7.RateLecturer(lecturePhytonOpen_2, 6)
    best_student_8.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_9.RateLecturer(lecturePhytonOpen_2, 9)
    # Лекция 4
    best_student_1.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_2.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_3.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_4.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_5.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_6.RateLecturer(lecturePhytonOpen_2, 8)
    best_student_7.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_8.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_9.RateLecturer(lecturePhytonOpen_2, 9)
    # Лекция 5
    best_student_1.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_2.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_3.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_4.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_5.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_6.RateLecturer(lecturePhytonOpen_2, 8)
    best_student_7.RateLecturer(lecturePhytonOpen_2, 6)
    best_student_8.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_9.RateLecturer(lecturePhytonOpen_2, 10)
    # Лекция 6 
    best_student_1.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_2.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_3.RateLecturer(lecturePhytonOpen_2, 6)
    best_student_4.RateLecturer(lecturePhytonOpen_2, 9)
    best_student_5.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_6.RateLecturer(lecturePhytonOpen_2, 8)
    best_student_7.RateLecturer(lecturePhytonOpen_2, 6)
    best_student_8.RateLecturer(lecturePhytonOpen_2, 10)
    best_student_9.RateLecturer(lecturePhytonOpen_2, 9)
    # Блок GIT
    # Лекция 1
    best_student_1.RateLecturer(lectureGIT_1, 10)
    best_student_2.RateLecturer(lectureGIT_1, 8)
    best_student_3.RateLecturer(lectureGIT_1, 6)
    best_student_4.RateLecturer(lectureGIT_1, 6)
    best_student_5.RateLecturer(lectureGIT_1, 7)
    best_student_6.RateLecturer(lectureGIT_1, 8)
    best_student_7.RateLecturer(lectureGIT_1, 6)
    best_student_8.RateLecturer(lectureGIT_1, 10)
    best_student_9.RateLecturer(lectureGIT_1, 10)
    # Лекция 2
    best_student_1.RateLecturer(lectureGIT_2, 9)
    best_student_2.RateLecturer(lectureGIT_2, 8)
    best_student_3.RateLecturer(lectureGIT_2, 6)
    best_student_4.RateLecturer(lectureGIT_2, 8)
    best_student_5.RateLecturer(lectureGIT_2, 7)
    best_student_6.RateLecturer(lectureGIT_2, 8)
    best_student_7.RateLecturer(lectureGIT_2, 9)
    best_student_8.RateLecturer(lectureGIT_2, 10)
    best_student_9.RateLecturer(lectureGIT_2, 9)
    # Лекция 3
    best_student_1.RateLecturer(lectureGIT_3, 9)
    best_student_2.RateLecturer(lectureGIT_3, 8)
    best_student_3.RateLecturer(lectureGIT_3, 6)
    best_student_4.RateLecturer(lectureGIT_3, 9)
    best_student_5.RateLecturer(lectureGIT_3, 7)
    best_student_6.RateLecturer(lectureGIT_3, 8)
    best_student_7.RateLecturer(lectureGIT_3, 6)
    best_student_8.RateLecturer(lectureGIT_3, 10)
    best_student_9.RateLecturer(lectureGIT_3, 9)
    # Лекция 1
    best_student_1.RateLecturer(lectureGIT_4, 9)
    best_student_2.RateLecturer(lectureGIT_4, 4)
    best_student_3.RateLecturer(lectureGIT_4, 6)
    best_student_4.RateLecturer(lectureGIT_4, 3)
    best_student_5.RateLecturer(lectureGIT_4, 7)
    best_student_6.RateLecturer(lectureGIT_4, 8)
    best_student_7.RateLecturer(lectureGIT_4, 6)
    best_student_8.RateLecturer(lectureGIT_4, 10)
    best_student_9.RateLecturer(lectureGIT_4, 9)
    # Лекция 1
    best_student_1.RateLecturer(lectureGIT_5, 9)
    best_student_2.RateLecturer(lectureGIT_5, 8)
    best_student_3.RateLecturer(lectureGIT_5, 6)
    best_student_4.RateLecturer(lectureGIT_5, 8)
    best_student_5.RateLecturer(lectureGIT_5, 10)
    best_student_6.RateLecturer(lectureGIT_5, 10)
    best_student_7.RateLecturer(lectureGIT_5, 6)
    best_student_8.RateLecturer(lectureGIT_5, 10)
    best_student_9.RateLecturer(lectureGIT_5, 9)
enter_Grades_lections()

print()
print('подсчет среднего балла у лекторов по предмету') 
intro_python_course.GetAverageLecturerRating()
print()
python_course.GetAverageLecturerRating()
print()
git_course.GetAverageLecturerRating()
print()

print('Делаем подсчет среднего балла по предмету у студентов')
python_course.GetAverageHomeworkGrade()
print()
intro_python_course.GetAverageHomeworkGrade()
print()
git_course.GetAverageHomeworkGrade()
print()

print('Выводим информацию о студентах')
print(best_student_1)
print()
print(best_student_3)
print()
print(best_student_5)
print()
print(best_student_7)
print()

print('Выводим информацию о лекторах')
print(cool_lecturer_1)
print()
print(cool_lecturer_2)
print()
print(cool_lecturer_3)
print()
print('Выводим информацию о экспертах')
print(best_reviewer)
print()

print('Сравниваем студентов')
print(best_student_1.GetAverageHomeworkGrade() == best_student_3.GetAverageHomeworkGrade())
print(best_student_1.GetAverageHomeworkGrade() > best_student_3.GetAverageHomeworkGrade())
print(best_student_1.GetAverageHomeworkGrade() < best_student_3.GetAverageHomeworkGrade())
print('Сравниваем лекторов')
print(cool_lecturer_1.GetAverageRating() == cool_lecturer_2.GetAverageRating())
print(cool_lecturer_1.GetAverageRating() > cool_lecturer_2.GetAverageRating())
print(cool_lecturer_1.GetAverageRating() < cool_lecturer_2.GetAverageRating())




