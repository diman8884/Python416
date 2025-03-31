# 20.03

# dom
# def negative_number(n): # [шаг1 -2, шаг2 3, шаг3 8, шаг4 -11, шаг5 -4, шаг6 6] после всех циклов пустой список в итоге
#     if not n: # if len(n) == 0
#         return 0
#     count = 0 # 0 или 1
#     if n[0] < 0:
#         count += 1
#     return count + negative_number(n[1:]) # 1 + 0 + 0 + 1 + 1 + 0
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negative_number(lst))
#
# print("Текст в локальном репозитории")

# 25.03

# print("Код написан на новом устройстве")

# файлы

# f = open("text.txt")
# print(*f)
# print(f)

# 27.03

# f = open("xyz.txt", "w")
# f.write("This is Line1.\nThis is Line2.\nThis is Line2.\n")
# f.close()

# f = open("xyz.txt")
# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open("xyz.txt")
# print(f.readlines(25))
# print(f.readlines())
# f.close()

# f = open("xyz.txt")
# for line in f:
#     print(line)
# f.close()

# lines = ["This is line1.\n", "This is line2.\n", "This is line3.\n"]
#
# f = open("lines.txt", "w")
# f.writelines(lines)
# f.close()

# lines = [str(i) for i in range(10, 1000, 15)]
# print(lines)
# f = open('lines.txt', 'w')
# for index in lines:
#     f.write(index + '\t')
# f.close()

# file = 'text2.txt'
# f = open(file, 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
# f = open(file, 'r')
# read_line = f.readlines()
# print(read_line)
# read_line[1] = "Hello world!\n"
# print(read_line)
# f.close()
#
# f = open(file, 'w')
# f.writelines(read_line)
# f.close()

# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.tell())# возвращает текущую позицию условного курсора в файле
# print(f.seek(1)) # перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open('test.txt', 'a')
# print(f.write("i am learning Python"))
# f.close()

# f = open('test.txt', 'w')
# print(f.write("i am learning Python"))
# f.close()

# f = open('test.txt', 'w')
# f.close()

# f = open('test3.txt', 'r+')
# print(f.write("i am learning Python"))
# f.close()
#
# f = open('test5.txt', 'a')
# print(f.write("i am learning Python"))
# print(f.seek(0))
# print(f.write("--new string--"))
# # print(f.read())
# f.close()

# with open ('text.txt', 'w') as f:
#     print(f.write("0123456789"))
# print(f.closed)

# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.04]
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
# print(get_line(lst))
# with open('res.txt', 'w') as f:
#     f.write(get_line(lst))
# print('Конец программы')

# with open('res.txt') as f:
#     nums = f.read()
#
# print(nums)
#
# print(map(float, nums.split()))
# print(list(map(float, nums.split())))
# print(sum(list(map(float, nums.split()))))
# print(sum(map(float, nums.split())))


# with open('res2.txt', 'w') as f:
#     f.write("Файл — именованная область данных на носителе информации, используемая как базовый объект "
#     "с данными в операционных системах.")# взаимодействие
#
# def longest_worlds(file):
#     with open(file) as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
# print(longest_worlds("res2.txt"))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# with open("one.txt", "w") as f:
#     f.write(text)
#
# with open('one.txt', 'r') as fr, open('two.txt', 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)

# import os
#
# print(os.getcwd()) # путь к действующим директориям
#
# print(os.listdir()) # возвращает список директорий
# print(os.listdir('..'))
# print(os.listdir('.venv'))

import os
# os.mkdir('folder')# создать папку
# os.rmkdir('folder.txt') # удалить папку

# os.makedirs('nested1/nested2/nested3') # создает директорию с подпапками

os.rename('two.txt', 'www.txt') # переименовать файл

os.rename("www.txt", "folder/www.txt") # переместить файл в заданную папку

os.renames("text4.txt", "test/text4.txt") #