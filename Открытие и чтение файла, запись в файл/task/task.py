# Задание 1,2
def GetShopListByDishes(dish, persons:int):
    cook_book = {} #{recept: [ ingredient_name : ingredient, quantity : int, measure : str ] }
    with open('Открытие и чтение файла, запись в файл/task/cookbook.txt', 'r') as file:
        for line in file: 
            cook_book[line.strip('\n')] = []            
            quantity_ingredients_in_recepts = file.readline()
            for ingredients_in_recept in range(int(quantity_ingredients_in_recepts)):
                number_ingredients = file.readline()
                ingredient, quantity, things =  number_ingredients.strip('\n').split(' | ')
                cook_book[line.strip('\n')] += [{'ingredient_name': ingredient, 'quantity': int(quantity), 'measure': things}]
            empty_line = file.readline()            
    #расчет ингридиентов для блюда
    for recept in dish:
        if recept in cook_book.keys():
            print(recept)
            for ingredient in cook_book[recept]:
                n = ingredient['quantity'] 
                ingredient['quantity'] = n * persons
                print(ingredient['ingredient_name'],':', ingredient['quantity'], ingredient['measure'])          
    file.close()

GetShopListByDishes(['Peking Duck', 'Fajitas'], 4)
print()

# Задание 3 (Не совсем понял что необходимо сделать)
def GetCountLines():
    text_all = {}
    with open('Открытие и чтение файла, запись в файл/task/1.txt', 'r') as text_1:
        countltne_1 = text_1.readlines()
        lengthLineText_1 = len(countltne_1)
        text_all[lengthLineText_1] = '1.txt'
        text_1.close()
    with open('Открытие и чтение файла, запись в файл/task/2.txt', 'r') as text_2:
        countltne_2 = text_2.readlines()
        lengthLineText_2 = len(countltne_2)
        text_all[lengthLineText_2] = '2.txt'
        text_2.close()
    with open('Открытие и чтение файла, запись в файл/task/3.txt', 'r') as text_3:
        countltne_3 = text_3.readlines()
        lengthLineText_3 = len(countltne_3)
        text_all[lengthLineText_3] = '3.txt'
        text_3.close()
    sorted_text = dict(sorted(text_all.items()))     
    for key in sorted_text.keys():
        for repet in range(int(key)):
            print(f'Строка номер {repet+1} файла номер {sorted_text[key]}')
        
GetCountLines()