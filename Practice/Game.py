import random
class Game:
    def __init__ (self):
        self.items = {} # Название предмета:[{Часть тела: str, урон: int}]
    
    def GetDeliveryItems(self):
        with open('Practice\items.txt', 'r', encoding='utf-8') as file_items:
            for items in file_items:
                self.items[items.strip('\n')] = []
                item = file_items.readline()
                description, dmg, defense, price = item.strip('\n').split(' | ')
                self.items[items.strip('\n')] = [{'Часть тела': description, 'Урон': dmg, 'Защита': defense, 'Цена': price}]
        file_items.close()
    
    def CheckInventory(self):
        for items_name in player.inventory:
            for game_items in self.items:
                if items_name == game_items:
                    for description in self.items[items_name]:
                        if int(description['Урон']) == 0:
                            if items_name in player.armor_items.keys():
                                player.armor_items[items_name] = int(player.armor_items[items_name]) + 1
                            else:
                                amount = 1
                                player.armor_items[items_name] = amount 
                        elif int(description['Защита']) == 0:
                            if items_name in player.weapon_items.keys():
                                player.weapon_items[items_name] = int(player.weapon_items[items_name]) + 1
                            else:
                                amount = 1
                                player.weapon_items[items_name] = amount
        
        def CheckArmors():
            print('\nБроня в инвентаре:')                       
            for armor, amount_armor in player.armor_items.items():
                for item in self.items:
                    if armor == item:
                        for description in self.items[armor]:
                            print(f'{armor} {amount_armor} шт. | Защита =', description['Защита'],f'| Цена =', description['Цена'])
                    
        def CheckWeapons():
            print('\nОружие в инвентаре:')
            for weapon, amount_weapon in player.weapon_items.items():
                for item in self.items:
                    if weapon == item:
                        for description in self.items[weapon]:
                            print(f'{weapon} {amount_weapon} шт. | Атака =', description['Урон'],f'| Цена =', description['Цена'])
                
        CheckArmors()
        CheckWeapons()
class Shop:
    def GetSellBy(self):
        print('Вы встречаете продавца!')

class Monstr:
    def Battle(self):
       print('На Вас выпрыгивает монстр!') 

class Dangerous:
    def EnterDangerous(self):
        print('Вы находите вход в подземелье')

class Player:
    lvl = {100:1, 300:2, 600:3, 1200:4}
    def __init__(self, name, hp, gold, game) -> None:
        self.name = name
        self.hp = hp
        self.gold = gold
        self.game = game
        self.exp = []
        self.equipment = {'Правая рука':'', 'Левая рука':'','Голова':'','Туловище':'', 'Ноги':''}
        self.inventory = ['Крышка от кастрюли', 'Палка', 'Ведро'] 
        self.armor_items = {}
        self.weapon_items = {}
        
    def Move(self):
        step = random.randint(1, 50)
        if step == 1 or step == 49:
            shop.GetSellBy()
        if step == 4 or step == 46:
            monstr.Battle()
        if step == 50:
            dangerous.EnterDangerous()
        else:
            print('Ищем приключения!\n')
            
    def GetEquipItems(self):
        listarmor = {}
        listweapon = {}
        
                         
        def EquipArmor():
            game.CheckInventory()
            if len(self.armor_items) == 0:
                print('К сожалению у вас нет предметов для экипирования')
            else:
                print('\nКакой предмет вы желаете экипировать?')
                 
                for step,  armor in enumerate(self.armor_items):
                    listarmor[step + 1] = armor
                    print(step + 1, '-' ,armor)
                command = int(input())
                
                if int(command) in listarmor.keys():
                    for items in game.items.keys():
                        if listarmor[command] in items:
                            for description in game.items[items]:
                                for description_equipment in self.equipment.keys():
                                    if description['Часть тела'] == description_equipment:
                                        if len(self.equipment[description_equipment]) == 0:
                                            self.equipment[description_equipment] = listarmor[command]
                                            self.inventory.remove(listarmor[command])
                                            self.armor_items.pop(armor)
                                            
                                            
                                        else:
                                            self.inventory.append(self.equipment[description_equipment])
                                            self.equipment[description_equipment] = listarmor[command]
                                            self.inventory.remove(listarmor[command])
                                             
                                      
        def EquipWeapon():
            game.CheckInventory()        
            print('\nКакой предмет вы желаете экипировать?')
            for step,  weapon in enumerate(self.weapon_items):
                listweapon[step + 1] = weapon
                print(step +1, '-', weapon)
                command = int(input())
                if int(command) in listweapon.keys():
                    for items in game.items.keys():
                        if listweapon[command] in items:
                            for description in game.items[items]:
                                for description_equipment in self.equipment.keys():
                                    if description['Часть тела'] == description_equipment:
                                        if len(self.equipment[description_equipment]) == 0:
                                            self.equipment[description_equipment] = listweapon[command]
                                            self.inventory.remove(listweapon[command])
                                            self.weapon_items.pop(weapon)
                                        else:
                                            self.inventory.append(self.equipment[description_equipment])
                                            self.equipment[description_equipment] = listweapon[command]
                                            self.inventory.remove(listweapon[command])
                                            self.weapon_items.pop(weapon)
        while True:
            print(f'\nЭкипировка на персонаже:\n{self.equipment}')
            command = input('\nЧто вы желаете экипировать?\n1 - Броня\n2 - Оружие\n')
            if command == '1':
                EquipArmor()
            if command == '2':
                EquipWeapon()
                
                
            

# Экземпляры класса
game = Game()
player = Player('None', 10, 3, game)
monstr = Monstr()
shop = Shop()
dangerous = Dangerous()


game.GetDeliveryItems()
# player.GetEquipItems()
while True:
    game.CheckInventory()
    print(player.armor_items)
    command = input('Введите команду:\n').lower()
    if command == 'i':
        game.GetDeliveryItems()
    if command == 'ad':
        player.GetEquipItems()
    else:
        player.Move()
        