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

# import os
# # os.mkdir('folder')# создать папку
# # os.rmkdir('folder.txt') # удалить папку
#
# # os.makedirs('nested1/nested2/nested3') # создает директорию с подпапками
#
# os.rename('two.txt', 'www.txt') # переименовать файл
#
# os.rename("www.txt", "folder/www.txt") # переместить файл в заданную папку
#
# os.renames("text4.txt", "test/text4.txt") #

#01.04

# f = open("test3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
# f = open("test3.txt", "r")
# read_line = f.readlines()
# print(read_line)
# f.close()
#
# pos1 = int(input("pos1 = "))
# pos2 = int(input("pos2 = "))
#
# if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
#     read_line[pos1], read_line[pos2] = read_line[pos2],  read_line[pos1]
# else:
#     print("Такой строки нет")
#
# print(read_line)
#
# f = open("test3.txt", "w")
# f.writelines(read_line)
# f.close()

# import os
#
# # print(os.walk("nested1"))
# # for root, dirs, files in os.walk("nested1", topdown=False):
# #     print("Root:", root)
# #     print("\tdirs:", dirs)
# #     print("\tFiles:", files)
#
# # import os.path
#
# print(os.path.split(r"E:\Python416\nested1\nested2\nested3\text5.txt"))
#
# print(os.path.join("nested1", r"E:\Python416", "nested2", "nested3", "text5.txt"))


# import os
#
# dirs = [r"Work\F1", r"Work\F2\F21"]
# # for d in dirs:
# #     os.makedirs(d)
#
# files = {
#     "Work": ["w.txt"],
#     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
#     r"Work\F2\F21": ["f211.txt", "f212.txt"]
# }
#
# for d, files in files.items():
#     for file in files:
#         file_path = os.path.join(d, file)
#         # print(file_path)
#         open(file_path, "w").close()
#
#
# file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
#
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"Такой-то текст в файле {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root1, directory, file_name in os.walk(root, topdown):
#         print(root1)
#         print(directory)
#         print(file_name)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)

# import os
# import time
#
# # print(os.path.exists(r"nested1\nested2\nested3\text5.txt"))
# # print(os.path.isfile(r"nested1\nested2\nested3\text5.txt"))
# # print(os.path.isdir(r"nested1\nested2\nested3"))
#
# file = "main.py"
#
# print(os.path.getsize(file))  # размер файла в байтах
# print(os.path.getatime(file))  # возвращает время последнего доступа к файлу
# print(os.path.getmtime(file))  # возвращает время последнего изменения файла
# print(os.path.getctime(file))  # возвращает время создания файла
#
# kb = os.path.getsize(file)
# a = os.path.getatime(file)
# m = os.path.getmtime(file)
# c = os.path.getctime(file)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c)))
# print(kb // 1024)

# class Point:
#     x = 1  # 100
#     y = 2
#
#
# p1 = Point()
# p1.x = 10
# p1.y = 20
# # Point.x = 100
# print(p1.x, p1.y)
# print(p1.__dict__)
#
# p2 = Point()
# print(p2.x, p2.y)
# p2.x = 5
# print(p2.__dict__)
#
# print(Point.__dict__)

# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 2
#
#     def set_coord(self, x1, y1):
#         self.x = x1
#         self.y = y1
#
#
# p1 = Point()  # экземпляр класса (объект)
# p1.set_coord(5, 3)
# print(p1.__dict__)
# # print(Point.__doc__)
# # print(Point.__dict__)
# print(type(p1))
# print(type(5))
# # p1.x = 5
# # p1.y = 10
# # p1.set_coord(5, 10)
# # print(p1.__dict__)
# # print(p1.x)
# # # Point.set_coord(p1, 20, 30)
# # # print(p1.__dict__)
# # #
# p2 = Point()
# p2.set_coord(100, 200)
# # print(p2.__dict__)
# print(p2.x)
