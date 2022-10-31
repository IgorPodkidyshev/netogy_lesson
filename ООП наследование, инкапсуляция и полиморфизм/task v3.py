class Course:

    def __init__(self, name):
        self.name = name
        self.students = [] # Список студентов проходящих данный курс  best_student_1, best_student_2 т тд
        self.lectures = [] # Список lectures class Lecture 
        self.homeworkGrades = {} #class Student: int[] оценки студентов за домашнее задание 
        self.isFinished = False
        self.FinishedCourse = [] # Законченные блоки
        

    def GetAverageHomeworkGrade(self) -> float: #Проходиться в словаре  homeworkGrades и вычислять среднюю оценку студента в ключь добавляем сумму оценок, в значение добавлем колличетсво оценок. 
        sum = 0
        num = 0
        return sum / num

    def GetAverageLecturerRating(self) -> float: #Проходиться по списку лекций и считает средний рейтинг для каждого лектора
        pass

    def Finishedcourse(self, student):
        pass 

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
        return f'Фамилия: {self.firstName}\nИмя: {self.lastName}'

    __repr__ = __str__

class Student(SchoolPerson):
    
    def start_group(self, student, block):
        if student in block:
            started_blocks[block] = student
        else:
            print('Error')

    def RateLecturer(self, lecture ,rating:int): #lecturer: Lecturer, mark: Int
        
        if rating <= 10 and rating >= 0:
            lecture.ratings[self] = rating 
        else:
            print('Error')

    def GetAverageHomeworkGrade(self) -> float: 
        pass
    def __getCourses(self, isFinished) -> list: #isFinished: Bool # -> corses[]
        pass
    def GetCurrentCourses(self, student) -> list: # -> corses[]
        # 1.1 проверяем есть ли студент в блоке лекций intro
        pass
        # 2. если есть делаем принт тмени блока
        # 1.2 проверяем есть ли студент в блоке лекций phyton
        # 1.3 проверяем есть ли студент в блоке лекций git
        #  
    def GetFinishedCourses(self) -> list: # -> corses[]
        self.isFinished = True
        return
    def __cmp__(self, other):
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

student_group_python = [best_student_1, best_student_2, best_student_3, best_student_4, best_student_5, best_student_6, best_student_7, best_student_8, best_student_9]
student_group_git = [best_student_1, best_student_2, best_student_3, best_student_4, best_student_5, best_student_6, best_student_7, best_student_8, best_student_9]
student_group_intro_python = [best_student_1, best_student_2, best_student_3, best_student_4, best_student_5, best_student_6, best_student_7, best_student_8, best_student_9]

started_blocks = {}



    

print(started_blocks)