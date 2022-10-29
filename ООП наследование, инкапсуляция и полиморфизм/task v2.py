class Student:
    def __init__(self, surname, name,  group):
        self.surname = surname
        self.name = name
        self.group = group
        self.grade = {}

    def info(self):
        print(self.name, self.surname, 'Группа - ', self.group)

        

    #Выставлние оценки и добавление курсов в словарь grade
    def enter_grade(self):
        if self.name not in self.grade:
            self.grade['Name'] = self.name
        cours = input('Введите курс: ')
        if cours in self.grade:
            print('Данный курс уже существует в карточке Студента - ', self.name)
        else:
            self.grade[cours]
        grade = int(input('Введите оценку: '))
        if grade <= 10:
            self.grade[cours] = grade
        else:
            print('Оценка может Быть не больше 10 баллов')
        print('Оценка', grade, 'успешно добавленна для курса', cours)
        return

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.groups = {'phyton': '', 'git': ''}

    # добавление группы для закрепления за лектором
    def add_group(self):
        metter = input('Введите предмет: ').lower()
        if metter in self.groups:
            group = input('Введите  группу для привязки к лектору: ')
            self.groups[metter] = group 
            print(lector_1.groups)
        else:
            print('Данный курс не существует в карточке')

    # добавление оценок
    def add_grade(self):
        cours = input('Введите курс: ')
        if cours in self.courses_attached:
            grade = int(input('Введите оценку: '))
            self.courses_attached[cours] = grade
        else:
            print('Данный курс не существует в карточке  - ', self.name)

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def add_grade(self):
        super().add_grade()
    
class Reviewer(Mentor):
    pass


# Список студентов
best_student_1 = Student('Иванов', 'Иван', 'G-66')
best_student_2 = Student('Мельникова', 'Ксения', 'G-66')
best_student_3 = Student('Ардаков', 'Игорь', 'G-66')
best_student_4 = Student('Донченко', 'Иван', 'G-66')
best_student_5 = Student('Кулагина', 'Юлия', 'G-66')
best_student_6 = Student('Бирюков', 'Евгений', 'G-67')
best_student_7 = Student('Васильев', 'Валерий', 'G-67')
best_student_8 = Student('Дылдин', 'Алексей', 'G-67')
best_student_9 = Student('Девин', 'Игорь', 'G-67')
best_student_10 = Student('Иванов', 'Иван', 'G-67')

# Список лекторов
lector_1 = Lecturer('best', 'lector Phyton')
lector_2 = Lecturer('best', 'lector Phyton')
lector_2 = Lecturer('best', 'lector GIT')


best_student_1.info()


lector_1.name
lector_1.surname

print(lector_1.groups)
lector_1.add_group()
    
                        