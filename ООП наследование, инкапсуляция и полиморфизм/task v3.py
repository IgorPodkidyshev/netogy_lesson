lecturesPhyton = {} # course :lecture
lecturesGIT = {}
studentInfo = {} #'Name':'Group'
studentGrade = {}

class Course:
    def __init__(self, course):
        self.course = course
    
    def addCourse(self, ):
        lectures[self.course] = ''
        print(lectures)
         
class Lecture:
    def __init__(self, lecture):
        self.lecture = lecture

    def addLecturesPhyton(self, ):
        lecturesPhyton[self.lecture] = ''
        

    def addLecturesGIT(self, ):
        lecturesGIT[self.lecture] = ''
        

class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.grade = {}

    def info(self):
        studentInfo[self.name] = self.group
        print(studentInfo)
    
    def AddGrade(self, cours, llecture, grade):
        
        

#Список студентов
# Предметы группы G-66 Питон и ГИТ
best_student_1 = Student('Иванов Иван', 'G-66')
best_student_2 = Student('Мельникова Ксения', 'G-66')
best_student_3 = Student('Ардаков Игорь', 'G-66')
best_student_4 = Student('Донченко Иван', 'G-66')
best_student_5 = Student('Кулагина Юлия', 'G-66')
# Предметы группы G-67 С++ и С#
best_student_6 = Student('Бирюков Евгений', 'G-67')
best_student_7 = Student('Васильев Валерий', 'G-67')
best_student_8 = Student('Дылдин Алексей', 'G-67')
best_student_9 = Student('Девин Игорь', 'G-67')
best_student_10 = Student('Иванов Иван', 'G-67')

# Список лекций 
    # 1. Знакомство с Python
lecturePhyton_1 = Lecture('Python. Знакомство с консолью')
lecturePhyton_2 = Lecture('Условные конструкции. Операции сравнения')
lecturePhyton_3 = Lecture('Введение в типы данных')
lecturePhyton_4 = Lecture('Циклы')
lecturePhyton_5 = Lecture('Коллекции данных. Словари. Множества.')
lecturePhyton_6 = Lecture('Функции - использование встроенных и создание собственных')
lecturePhyton_7 = Lecture('ООП: объекты и классы. Взаимодействие между ними')
lecturePhyton_8 = Lecture('ООП: наследование, инкапсуляция и полиморфизм')
        # 2. Работа с файловой системой в Python
lecturePhyton_9 = Lecture('Открытие и чтение файла, запись в файл')
lecturePhyton_10 = Lecture('Работа с разными форматами данных')
        # 3. Работа с внешним API
lecturePhyton_11 = Lecture('Работа с библиотекой requests, http запросы')
lecturePhyton_12 = Lecture('Работа с классами на примере API VK')
        # Курсовой проект
lecturePhyton_13 = Lecture('Защита курсового проекта PY')
    # Git — система контроля версий
lectureGIT_1 = Lecture('1. Знакомство с системой контроля версий Git')
lectureGIT_2 = Lecture('2. Работа с локальным репозиторием в Git')
lectureGIT_3 = Lecture('3. Работа с удаленным репозиторием через GitHub')
lectureGIT_4 = Lecture('4. Командная работа в Git и GitHub')
lectureGIT_5 = Lecture('5. Командная работа в Git и GitHub. Часть 2')


coursePhytonOpen = Course('Вводный модуль для студентов профессий PD и FPY')
coursePhyton = Course('Python-разработчик с нуля') 
courseGIT = Course('Git — система контроля версий') 

lecturePhyton_1.addLecturesPhyton()
lecturePhyton_2.addLecturesPhyton()
lecturePhyton_3.addLecturesPhyton()
lecturePhyton_4.addLecturesPhyton()
lecturePhyton_5.addLecturesPhyton()
lecturePhyton_6.addLecturesPhyton()
lecturePhyton_7.addLecturesPhyton()
lecturePhyton_8.addLecturesPhyton()
lecturePhyton_9.addLecturesPhyton()
lecturePhyton_10.addLecturesPhyton()
lecturePhyton_11.addLecturesPhyton()
lecturePhyton_12.addLecturesPhyton()
lecturePhyton_13.addLecturesPhyton()
print(lecturesPhyton)

lectureGIT_1.addLecturesGIT()
lectureGIT_2.addLecturesGIT()
lectureGIT_3.addLecturesGIT()
lectureGIT_4.addLecturesGIT()
lectureGIT_5.addLecturesGIT()
print(lecturesGIT)


# best_student_1.info()
# best_student_2.info()
# best_student_3.info()
# best_student_4.info()
# best_student_5.info()
# best_student_1.info()

        # данные студента:
        # 1.ФИО 
        # 2.Группа
        # 3.Предметы которые проходит
        # 4.Оценки за предметы
        # 3,4 = словарю где будет написанно в ключе предмет, а в значении оценка

        # данные лектора:
        # 1.ФИО
        # 2.Группы кторые он ведет
        # 3.Предметы которые он ведет
        # 4.Оценки от студентов по лекциям
        # 3,4 = словарю где будет написанно в ключе предмет, а в значении оценка

        # данные эксперта:
        # 1.ФИО
        
        # 1.Словарь студента Группа:ФИО
        # 2.