class Character:
    name = ''
    heals = 100
    power = 1
    energy = 100
    eat = 10
    attack = power // 2

    # Теринировка
    def workout(self, hour):
        if self.energy >= 10 and self.eat >= 2:
            self.energy -= hour * 10
            self.eat -= hour *2
            self.energy += hour * 2
            print()
        elif self.energy < 10:
            print('You are very tired, go to bed')
        elif self.energy < 2:
            print('you are very hungry, go eat')
    # Сон
    def sleep(self, hour):
        if self.energy <= 94 and self.eat >= 8:
            self.eat -= hour * 2
            self.energy += hour * 6
        elif self.energy > 98:
            print('You feel rested')
        elif self.eat < 2:
            print('you are very hungry, go eat')    
    # Еда
    def food(self, meat):
        if self.eat <= 8 and self.energy >= 2:
            self.eat += meat * 4
            self.energy -= meat * 2
        elif self.eat > 6:
            print('you are not hungry')

    # Смена имени
    def naming(self, rename):
        self.name = rename
    
gamer = Character()

help = """"
eat - reduce hunger, but increase fatigue.
training - increase strength but decrease energy.
rename - change name.
sleep - increase energy but increase hunger."""

# Переписать print в саму функцию выводит ерунду! не устраивает. 
# переделать функцию чтобы не давал насыщения и отдыха больше начальных значений, проверяя каждый раз чтобы игрок не превысил данное число, 

while True:
    command = (input('enter command: '))
    if command == 'help':
        print(help)
    elif command == 'eat':
        n_meat = int(input('how much meat do you want to eat: '))
        gamer.food(n_meat)
        print('you ate', n_meat, 'pieces of meat')
        print('eat = ', gamer.eat)
        print('energy = ', gamer.energy)
    elif command == 'training':
        hour = int(input('how many hours do you want to exercise: '))
        gamer.workout(hour)
        print('you trained for ', hour, ' hours')
        print('power = ', gamer.power)
        print('eat = ', gamer.eat)
        print('energy = ', gamer.energy)


            