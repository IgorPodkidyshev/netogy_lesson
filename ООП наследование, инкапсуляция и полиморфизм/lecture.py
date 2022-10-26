# # Первая лекция ООП
# class Character:
#     def __init__(self, name, power, energy = 100, hand = 2):
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self.backpack = []
#         self.hand = hand

#     def change_alies(self, new_alies):
#         self.alies = new_alies

#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('not hungry')
    
#     def workout(self, fatigue):
#         if self.energy > 0:
#             self.energy -= fatigue * 4
#             self.power += fatigue * 2
#             print('Energy', self.energy)
#             print('Power', self.power)
            
#         else:
#             print('You are very tired')

#     def beat_up(self, foe):
#         if not isinstance(foe, Character):
#             return
#         if foe.power < self.power:
#             foe.status = 'defeated'
#             self.status = 'wimmer'
#         else:
#             print('Retreat!')

class Character:
    def __init__(self, name = 'Peter Parker', power = 80, energy = 100, hands = 2):
        self.name = name
        self.power = power
        self.energy = 100
        self.hands = 2
        self.backpack = []
    
    def attack(self, foe):
        foe.health -= 10
        
    #move
    def move(self):
        print('Moving on 1 square')

class Spider:
    def __init__(self, power = 0, energy = 50, hands = 8):
        self.power = power
        self.energy = energy
        self.hands = hands

    def webshoot(self):
        print('Pew-pew')

    def attack(self, foe):
        foe.status = 'stunned'

    #move
    def move(self):
        self.webshoot()
        print('Moving on 2 square')

class SpaiderMan(Character, Spider):
    def __init__(self, name='Peter Parker', power=80, energy=100, hands=2):
        super().__init__(name, power, energy, hands)
        self.backpack = []
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20

    def webshoot(self):
        return super().webshoot()

    def move(self):
        self.webshoot()
        print('Moving on 3 square')

    def attack(self, foe):
        super().attack(foe)
        Spider.attack(self, foe)

    def __lt__(self, other):
        if not isinstance(other, Character):
            print('Not a Character!')
            return
        return self.power < other.power

    def __str__(self):
        res = f'Power Character {self.name}  = {self.power}'
        return res

man = SpaiderMan()
woman = SpaiderMan('Alice', 85)

print(man.name)
print(man.energy)
print(man.power)
print(man.hands)
print(man.backpack)
# man.webshoot()
man.move()

print()

enemy = Character('Some Enemy', 10)
enemy.health = 100

man.attack(enemy)

print(enemy.health)
print(enemy.status)

print(man < woman)

print()

print(man)
print(woman)


# # Получить список в каком порядке питом будет искать атрибуты методов
# print(SpaiderMan.mro())   