# # print(type('Hello, World!'))

# # print(dir(str))

# #Добавляем атрибуты нашему классу
# from turtle import distance


# class Character:
#     name = 'Peter'
#     power = 8
#     energy = 10
#     hands = 2

# # Обьект - отдельный представитель класса, имеющее конкретное состояние и поведение, полностью определяемое классом 
# peter = Character()

# # Вывести информацию об атрибутах в классе
# print(peter.power)
# print()

# # Посмотреть словарь нашего класса
# print(peter.__dict__)

# # Присваеваем атрибуты нашему классу
# peter.name = 'Spider Man'
# peter.power = 55
# #Добавляем новый атрибут нашему классу 
# peter.firstname = 'Parker'
# print(peter.firstname)

# # Посмотреть словарь нашего класса с новыми птрибутами. 
# print(peter.__dict__)

# batman = Character()
# batman.name = 'Брюс'
# batman.firstname = 'Уэйн'
# batman.alias = 'Бэтмен'
# batman.power = 60
# batman.character = 'Скверный'

# # Выводим информацию атрибутов с меткой бетмен
# print(batman.__dict__)

# #можно вызвать класс с атрибутами внесенными туда в "6" строке
# print(Character.__dict__)

# print(batman.name)
# print(batman.firstname)
# print(batman.alias)
# print("Сила", batman.power)
# print('Характер', batman.character)

# Создание методов(функций)
class Character:
    name = 'Peter Parker'
    power = 6
    energy = 100
    hands = 2

    def eat(self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print('not hungry')
    
    def workout(self, fatigue):
        if self.energy > 0:
            self.energy -= fatigue * 4
            self.power += fatigue * 2
            print('Energy', self.energy)
            print('Power', self.power)
            
        else:
            print('You are very tired')

# person = input("введите: ")
person = Character()

print(person.name, person.power, person.energy)

person.workout(1)
person.workout(2)
person.workout(4)
person.workout(8)