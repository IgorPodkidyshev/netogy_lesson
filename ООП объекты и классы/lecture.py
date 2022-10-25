# print(type('Hello, World!'))

# print(dir(str))

#Добавляем атрибуты нашему классу
class Character:
    name = 'Peter'
    power = 8
    energy = 10
    hands = 2

# Обьект - отдельный представитель класса, имеющее конкретное состояние и поведение, полностью определяемое классом 
peter = Character()

# Вывести информацию об атрибутах в классе
print(peter.power)
print()

# Посмотреть словарь нашего класса
print(peter.__dict__)

# Присваеваем атрибуты нашему классу
peter.name = 'Spider Man'
peter.power = 55
#Добавляем новый атрибут нашему классу 
peter.firstname = 'Parker'
print(peter.firstname)

# Посмотреть словарь нашего класса с новыми птрибутами. 
print(peter.__dict__)

batman = Character()
batman.name = 'Брюс'
batman.firstname = 'Уэйн'
batman.alias = 'Бэтмен'
batman.power = 60

# Выводим информацию атрибутов с меткой бетмен
print(batman.__dict__)

#можно вызвать класс с атрибутами внесенными туда в "6" строке
print(Character.__dict__)