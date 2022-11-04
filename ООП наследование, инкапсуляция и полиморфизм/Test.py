class Home:
    def __init__(self, numberStreet, numberHome, numberFloor, numberEntrance):
        self.numberHome = numberHome
        self.numberStreet = numberStreet
        self.numberEntrance = numberEntrance
        self.numberFloor = numberFloor
        self.entrances = [] # [Entrances]
        self.averege_age = {} # man: int, woman: int
    def __str__(self) -> str:
        return f'Улица: {self.numberStreet}\nДом: {self.numberHome}\nКолличество этажей: {self.numberFloor}\nКолличество подъездов: {self.numberEntrance}\n'

    def GetAverageGender(self):
        man = []
        woman = []
        for entrance in self.entrances:
            for flat in entrance.flats:
                for person in flat.persons:
                    if person.gender == 'man':
                        # man.extend(person.age)
                        print(person.name, person.age)
                        man.append(person.age)
                    if person.gender == 'woman':
                        print(person.name, person.age)
                        woman.append(person.age)
                        # woman.extend(person.age)
        print(man)
        print(woman)   

    __repr__ = __str__

class Entrance:
    def __init__(self, numberEntrance, numberFloor, numberFlat):
        self.numberEntrance = numberEntrance
        self.numberFloor = numberFloor
        self.numberFlat = numberFlat
        self.flats = [] # [Flat]

    def __str__(self) -> str:
        return f'Номер подъезда: {self.numberEntrance}\nКолличество этажей в подъезде: {self.numberFloor}\nКвартиры в подъезде: {self.numberFlat}\n'

    __repr__ = __str__

class Flat:
    def __init__(self, entrance, floor, numberFlat) -> None:
        self.entrance = entrance
        self.floor = floor
        self.numberFlat = numberFlat
        self.persons = []
        self.furnitures = []

    def __str__(self) -> str:
        return f'Квартира находится в подъезде №: {self.entrance}\nКвартира находится на {self.floor} этаже\nНомер квартиры: {self.numberFlat}\n'

    __repr__ = __str__ 

class Person:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'ФИО: {self.name}\nВозраст: {self.age}\nПол: {self.gender}\n'

    __repr__ = __str__

class Children(Person):
    pass

# Экземпляры класса
    # Home
home_1 = Home('Mira', 31, 2, 2)
    # Entrance
entrance_1 = Entrance(1, 2, '1-4')
entrance_2 = Entrance(2, 2, '5-8')
    # Flat (entrance, floor, numberFlat)
flat_1 = Flat(1, 1, 1)
flat_2 = Flat(1, 1, 2)
flat_3 = Flat(1, 2, 3)
flat_4 = Flat(1, 2, 4)
flat_5 = Flat(2, 1, 5)
flat_6 = Flat(2, 1, 6)
flat_7 = Flat(2, 2, 7)
flat_8 = Flat(2, 2, 8)
    # Person name, age, gender
        # man
person_man_1 = Person('Ivan Vasev', 31, 'man')
person_man_2 = Person('Vasilii Fedorov', 25, 'man')
person_man_3 = Person('Fedor Ivanov', 29, 'man')
person_man_4 = Person('Petro Genish', 49, 'man')
person_man_5 = Person('Igor Mihailov', 36, 'man')
person_man_6 = Person('Semen Oslov', 22, 'man')
        # womam
person_woman_1 = Person('Rita Vaseva', 33, 'woman')
person_woman_2 = Person('Anna Fedorova', 24, 'woman')
person_woman_3 = Person('Tatiana Ivanova', 27, 'woman')
person_woman_4 = Person('Katerina Mihailovna', 46, 'woman')
person_woman_5 = Person('Lena Ozerova', 38, 'woman')
person_woman_6 = Person('Olga Minecraftovna', 26, 'woman')
person_woman_7 = Person('Vaselisa Petrova', 19, 'woman')
    # Children

# Закрепляем все за всем
number_home_1_entrances = [entrance_1, entrance_1]

number_entrance_1_Flats = [flat_1, flat_2, flat_3, flat_4]
number_entrance_2_Flats = [flat_5, flat_6, flat_7, flat_8]

persons_flat_1 = [person_man_1, person_woman_1]
persons_flat_2 = [person_man_2, person_woman_2]
persons_flat_3 = [person_man_3, person_woman_3]
persons_flat_4 = [person_man_4]
persons_flat_5 = [person_woman_4, person_woman_6]
persons_flat_6 = [person_man_5]
persons_flat_7 = [person_woman_5]
persons_flat_8 = [person_man_6, person_woman_7]

# Добавляем закрепленные Массивы к обьектам класса
home_1.entrances.extend(number_home_1_entrances)
entrance_1.flats.extend(number_entrance_1_Flats)
entrance_2.flats.extend(number_entrance_2_Flats)

flat_1.persons.extend(persons_flat_1)
flat_2.persons.extend(persons_flat_2)
flat_3.persons.extend(persons_flat_3)
flat_4.persons.extend(persons_flat_4)
flat_5.persons.extend(persons_flat_5)
flat_6.persons.extend(persons_flat_6)
flat_7.persons.extend(persons_flat_7)
flat_8.persons.extend(persons_flat_8)

##Вызываем СТР всего дома
# print(home_1)
# print(entrance_1)
# print(flat_1)
# print(person_man_1)
# print(person_woman_1)

## Вызываем массивы в классах
# print(home_1.entrances)
# print()
# print(entrance_1.flats)
# print(entrance_2.flats)

# print(flat_1.persons)
# print(flat_5.persons)
# print(flat_8.persons)

home_1.GetAverageGender()