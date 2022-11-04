# # Метод 1 read() чтение файла
# f1 = open('Открытие и чтение файла, запись в файл/file1.txt')   #открываем файл 
# content = f1.read() # Читаем файл read()
# # print(content)
# # print(type(content))
# f1.close() #закрываем чтение файла, это обязательно!

# #Метод readline() построчное чтение
# f2 = open('Открытие и чтение файла, запись в файл/file1.txt')
# contentline = f2.readline()
# contentline_1 = f2.readline()
# # print(contentline,contentline_1)
# f2.close()

# # Метод readlines() считывает все строки типа list

# f3 = open('Открытие и чтение файла, запись в файл/file1.txt')
# res = f3.readlines()
# text = {}
# for slova in res:
#     text[n] = res
#     print(text)
#     # print(len(res))

# # print(res)
# f3.close

with open('Открытие и чтение файла, запись в файл/file1.txt', 'a') as document:
    document.write('\nHello World!\n')
with open('Открытие и чтение файла, запись в файл/file1.txt', 'a') as document:
    document.write('Hello World_1!\n')