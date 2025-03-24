# модули

# import math
#
# print(math.sqrt(4)) # корень
# print(math.ceil(3.2.)) # окружение в верхнюю сторону
# print(math. floor(3.8))

#
# print(m.sqrt(4)) # корень
# print(m.ceil(3.2.)) # окружение в верхнюю сторону
# print(m. floor(3.8)) # окружении в меньшую сторону

# from math import *
#
# print(sqrt(4)) # корень
# print(ceil(3.2.)) # окружение в верхнюю сторону
# print(floor(3.8)) # окружении в меньшую сторону

# from math import sqrt, ceil, floor
#
# print(sqrt(4)) # корень
# print(ceil(3.2)) # окружение в верхнюю сторону
# print(floor(3.8)) # окружении в меньшую сторону
# from math import pi
# #print(pi)
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * pi * radius, 2))

# import time
# import locale
#
# # print(time.time())
# # print(time.ctime(748863169))
# # print(time.localtime())
# # res = time.localtime()
# # print(res.tm_year, "-0", res.tm_mon, "-0", res.tm_mday, sep="")
# # print(time.strftime("today is %B %d, %Y"))
# # print(time.strftime("%m/%d/%Y, %H:%M:%S"))
# #
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y, %A"))

# import time

# start = time.monotonic()
# pause = 5
# print('Программа запущена')
# time.sleep(pause)
# result = time.monotonic() - start
# print('Программа выполнена за', result, 'секунд')

# a = 500
# for i in range(a, -1, -1):
#     time.sleep(1)
#     print(i)

# dom 11
# import math
#
# shape = int(input("Выбор фигуры:\n1-треугольник\n2-прямоугольник\n3-круг\n: "))
# s = None
# if shape == 1:
#     a = int(input("Введите сторону a = "))
#     b = int(input("Введите сторону b = "))
#     c = int(input("Введите сторону c = "))
#     p = (a + b + c) / 2
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
# elif shape == 2:
#     a = int(input("Введите сторону a = "))
#     b = int(input("Введите сторону b = "))
#     s = a * b
# elif shape == 3:
#     radius = int(input("Введите радиус = "))
#     s = math.pi + radius ** 2
# else:
#     print("Такой фигуры нет")
#
# print(round(s, 2))

# функции


# def hello(name, age):
#     print("Меня зовут " + str(name) + ". Мне " + str(age) + " лет.")
#
#
# hello("Irina", 28)
# hello("Ivan", 15)

# def get_sum(a, b):
#     print(a + b)
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")

# def print_line(count, a, b):
#     for i in range(count):
#         print(a, end="")
#     else:
#         print(b, end="")
#
#
# print_line(9, "+", "-")
# print_line(7, "X", "0")

# def get_sum(a, b):
#     return a + b
#
# x = 2
# y = 5
# res = get_sum(x,y)
# print(res)
#
#
# print(get_sum(5, 10))

# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
# x = 2
# y = 5
# res = get_sum(x,y)
# print(res)
#
#
# print(get_sum(5, 10))

# def max_value(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(max_value(9, 6))
# print(max_value(9, 16))

# def add(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# print(add(a, b))

# def change(lst):
#     lst[0], lst[-1] = lst[-1],lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#
#     lst.insert(0, end)
#     return lst  # return end
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def is_first_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(is_first_big(10, 5))
# # print(is_first_big(5, 10))
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if is_first_big(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше второго")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lover = True
#         if "0" <= ch <= "9":
#             has_num = True
#     if len(password) >= 8 and has_upper:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль. ")
# else:
#     print("Это ненадежный пароль. ")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
# print(get_sum(7, 9, d=3 , c=5))
# # print(get_sum(1, 5, 2, 7))
# # print(get_sum(1, 5, 2))
# # print(get_sum(1, 5))
# # print(get_sum(1, 5, 2))

# def display_info(name, age):
#     print("Name", name, "\nAge:", age)
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age = 23, name ="Ira")
