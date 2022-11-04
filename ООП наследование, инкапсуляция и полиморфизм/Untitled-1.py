class ClassList():
    def __init__(self):
        self.list = []

    def __str__(self):
        return self.list

    def append(self, ob):
        self.list.append(ob)

a = input("Введите данные: ").split(', ')
car = Car(a[0], a[1])
array = ClassList()
array.list.append(car)
# array.append(car_copy)

print(array.__str__())