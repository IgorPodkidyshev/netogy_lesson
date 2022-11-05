import random
class Player:
    def __init__(self, name, gender, race, profession): # race, profession,
        self.name = name
        self.gender = gender
        self.race = race
        self.profession = profession
        self.characteristics = [0, 0, 0, 0, 0, 0] # СИЛ, ЛОВ, ВЫН, ИНТ, МУДР, ХАР
        self.lvl = {}
        self.skills = {'Сила':{'Атлетика': 0, },
        'agility': {'Акробатика': 0, 'Ловкость рук': 0, 'Скрытность': 0},
        'intellect': {'История': 0, 'Магия': 0, 'Природа': 0, 'Ресследование': 0, 'Религия': 0},
        'sapience': {'Выживание': 0, 'Дрессировка': 0, 'Внимание': 0, 'Медицина': 0, 'Проницательность': 0},
        'charisma': {'Запугивание': 0, 'Исполнение': 0, 'Обман': 0, 'Убеждение': 0}}
        self.inventory = {'Деньги': 0}
    def __str__(self) -> str:
        return f'\n\nИмя персонажа: {self.name}\nПол персонажа: {self.gender}\nРаса: {self.race}\nКласс: {self.profession}\n\nСила: {self.characteristics[0]}\nЛовкость: {self.characteristics[1]}\nВыносливость: {self.characteristics[2]}\nИнтелект: {self.characteristics[3]}\nМудрость: {self.characteristics[4]}\nХаризма: {self.characteristics[5]}\n'
    def GetNewPlayer(self):
        skill_poin_bool = False
        number_random = []
        for roll in range(int(6)):
            roll = []
            for number in range(int(4)):
                number = random.randint(1,6)
                roll.append(number)    
            sort_roll = list(sorted(roll))
            sort_roll.pop(0)        
            number_random.append(sum(roll))        
        if skill_poin_bool == False:
            print(f'распределите очки навыков:\n')
            print(f'У вас имеются следующие очки:\n {number_random}\nДавайте распределим их:')
            for number in number_random:
                print(f'В какую харрактеристику Вы хотите положить {number_random[0]} очков навыка:\n1-СИЛА\n2-ЛОВКОСТЬ\n3-ВЫНОСЛИВОСТЬ\n4-ИНТЕЛЕКТ\n5-МУДРОСТЬ\n6-ХАРРИЗМА\n')
                skill_poin = input() 
                reply = int(skill_poin) - 1
                if self.characteristics[reply] <= 0:
                    print(type(reply))
                    self.characteristics[reply] = number_random[0]
                    number_random.pop(0)
                    print(self.characteristics)
                else: 
                    print('Вы уже вкладывади очки в это умения')
            skill_poin == True       
        # Задаем имя персонажа
        if self.name == 'None':
            new_name = input(f'Введите Имя: \n')
            if 3 < len(new_name) < 25:
                check_new_name = input(f'Вы желате схранить имя: {new_name} ?\n Введите "да или "нет"\n').lower()
                if check_new_name == "lf" or check_new_name == 'да':
                    self.name = new_name
                elif check_new_name == "нет" or check_new_name == 'ytn':
                    self.GetNewPlayer()
                else:
                    print('Введите "да или "нет"\n')
                    self.GetNewPlayer()
            else:
                print('Имя персонажа должно быть не более 25 символов и не менее 4')
                self.GetNewPlayer()
        # Задаем пол персонажа
        if self.gender == 'None':
            new_gender = input('Выберите пол  персонажа: \n1 - Женщина\n2 - Мужчина\n')
            if new_gender == '1':
                self.gender = 'Женщина'
            elif new_gender == '2':
                self.gender = 'Мужчина'
            else:
              self.GetNewPlayer()
        # Задаем рассу
        while self.race == 'None':
            races = {'человек': [1, 1, 1, 1, 1, 1], 'эльф': [0, 2, 0, 0, 0, 0], 'гном': [0, 0, 0, 2, 0, 0]}
            print("Чтобы ознакомиться со списком расс введите help")
            new_race = input('Введите рассу или help: \n').lower()
            if new_race in races.keys():
                print('Ваша расса :', new_race)
                self.race = new_race
                self.characteristics[0] += races[new_race][0]
                self.characteristics[1] += races[new_race][1]
                self.characteristics[2] += races[new_race][2]
                self.characteristics[3] += races[new_race][3]
                self.characteristics[4] += races[new_race][4]
                self.characteristics[5] += races[new_race][5]
            if new_race == 'help' or new_race == 'рудз':
                for race in races.keys():
                    print(f'{race}\n')
        # Задать класс
        while self.profession == 'None':
            professions = {'воин': [2, 0, 1, 0, 0, 0], 'колдун':[0, 0, 0, 2, 1, 0], 'плут':[0, 2, 0, 0, 0, 1], 'следопыт':[0, 2, 1, 0, 0, 0]}
            print("Чтобы ознакомиться со списком классов введите help")
            new_profession = input('Введите класс или help: \n').lower()
            if new_profession in professions.keys():
                print('Ваша Класс: ', new_profession)
                self.profession = new_profession
                self.characteristics[0] += professions[new_profession][0]
                self.characteristics[1] += professions[new_profession][1]
                self.characteristics[2] += professions[new_profession][2]
                self.characteristics[3] += professions[new_profession][3]
                self.characteristics[4] += professions[new_profession][4]
                self.characteristics[5] += professions[new_profession][5]
            elif new_profession == 'help' or new_race == 'рудз':
                for profession in professions.keys():
                    print(f'{profession}\n') 

        print(player)

    def GetNewLvl(self):
        pass

player = Player('None' , 'None', 'None', 'None')

player.GetNewPlayer()

while True:
    if player.name == 'None':
        player.GetNewPlayer
    command = input('Введите команду: ')
    if len(command) > 1:
        print('Иди ты нахуй со своими командами')
    if command == 'info':
        print(player)
    else:
        print('Че молчишь?')



    