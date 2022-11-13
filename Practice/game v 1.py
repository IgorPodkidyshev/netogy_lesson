game_items = {} #Часть тела, урон, защита, цена
listarmor = {}
listweapon = {}
empty_cell_equipment = []


def GetDeliveryItems():
        with open('Practice\items.txt', 'r', encoding='utf-8') as file_items:
            for items in file_items:
                game_items[items.strip('\n')] = []
                item = file_items.readline()
                description, dmg, defense, price = item.strip('\n').split(' | ')
                game_items[items.strip('\n')] = [description, int(dmg), int(defense), int(price)]
        file_items.close()

GetDeliveryItems()

class Player:
    def __init__ (self, name):
        self.name = name
        self.stat = [10, 0, 2, 2, 0, 0, 2, 10] # 0ХП, 1МП, 2СИЛ, 3ЛОВ, 4ИНТ, 5БРОНЯ, 6АТАКА, 7Золото
        self.inventory = {'Крышка от кастрюли' : 2, 'Палка' : 1, 'Ведро' : 1}
        self.equipment = {'Правая рука':'', 'Левая рука':'Щит','Голова':'','Туловище':'', 'Ноги':''}

    def CheckEquipment(self):
        for body_part, equipment in self.equipment.items():
            if len(equipment) == 0:
                empty_cell_equipment.append(body_part)
                

    def CheckStat(self):
        self.stat[6] = 2
        self.stat[5] = 0
        player.CheckEquipment()
        for equipment in self.equipment.values():
            if len(equipment) != 0:
                for items in game_items:
                    if equipment == items:
                        self.stat[6] += game_items[items][1] 
                        self.stat[5] += game_items[items][2]
    def ShowStat(self):
        print(f'Харрактеристики:\nХП - {self.stat[0]}\nСИЛА - {self.stat[2]}\nЛОВКОСТЬ - {self.stat[3]}\nЗАЩИТА - {self.stat[5]}\n АТАКА - {self.stat[6]}\n')

    def GetShowitems(self):
        player.CheckInventory()
        print('\nБроня в рюкзаке:')
        for step, armor in enumerate(listarmor):              
                print(f'{step + 1}) {armor} -', listarmor[armor][4], f'шт. | Защита -', listarmor[armor][2], '| Цена -', listarmor[armor][3]) 
        print('\nОружие в рюкзаке:')
        for step, weapon in enumerate(listweapon):              
                print(f'{step + 1}) {weapon} -', listweapon[weapon][4] ,f'шт. | Атака -', listweapon[weapon][1], '| Цена -', listweapon[weapon][3]) 
        print('\nЗелья:')
        
        print('\nЭкипированно:')
        for descriptions, equipment in self.equipment.items():
            if equipment == '':
                print(f'{descriptions} -  Не одето')
            else:
                print(f'{descriptions} -  {equipment}')

    def CheckInventory(self):
        for item in self.inventory.keys():
            for items in game_items.keys():
                if item == items:
                    game_items[item]
                    if int(game_items[item][1]) > 0:
                        listweapon[items] = game_items[item]
                        listweapon[items].append(self.inventory[item])
                    elif int(game_items[item][2]) > 0:
                        listarmor[items] = game_items[item]
                        listarmor[items].append(self.inventory[item])
      
    def GetEquipmentitems(self, type_equipment):
        player.CheckInventory()
        player.CheckEquipment()
        def replacement_items():                      
            self.inventory[items] = 1
            self.equipment[body_part] = name
            return                      
        def installation_items():               
            type_equipment.pop(name, index)                       
            self.inventory.pop(name_item, amount)
            return 
             
        print('Введите название предмета из списка для выбора:')
        for step, item in enumerate(type_equipment): 
            print(f'{step + 1}) {item} -', type_equipment[item][4] ,f'шт. | Атака -', type_equipment[item][1])
            type_equipment[item].append(step+1)
        command = int(input('Введите номер предмета из списка: '))
        for name, index in type_equipment.items():
            if command == index[5]:
                for body_part, items in self.equipment.items():
                    if len(items) == 0 and body_part == index[0]:
                        self.equipment[body_part] = name   
                        for name_item, amount in self.inventory.items():
                            print (f'Предмет {name} успешно добавлен!')
                            if name_item == name:
                                if int(amount) >= 2:
                                    self.inventory[name_item] = amount - 1
                                else:
                                    installation_items()
                    if len(items) >= 1 and body_part == index[0]:
                       for name_item, amount in self.inventory.items():
                           if items != name_item:
                            #    print (f'Предмет {name} успешно добавлен!')
                               
                            #    replacement_items()
                               
                        
                                
        
                             
       
    def MenuEquipmentItems(self):
        print('Экипирование брони\оружие')
        command = input(f'Что вы хотите экипировать?\n1 - Оружие\n2 - Броню')
        if command == '1':
            player.GetEquipmentitems(listweapon)
        if command == '2':
            player.GetEquipmentitems(listarmor)
                
                
        
                      

  
player = Player('None')

# player.GetShowitems()
player.GetEquipmentitems(listarmor)


while True:
    player.GetEquipmentitems(listarmor)
    player.ShowStat()          