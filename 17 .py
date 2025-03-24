# Строки

# print(bin(18)) #0b10010-двоичная система счисления
# print(oct(18)) # 0o22- восьмеричная система счисления
# print(hex(18))  #0x12 - шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010 + 4)

# unicode

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print("y" in e)
# print("a" in e)
# print(e[1])
# print(e[-1])
# print(e[1:3])

# def chang_char_to_str(s, old, new):
#     s2 = "" #"Я изучаю P ............P .........P"
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
# str1 = "Я изучаю Nython. Мне нравиться Nython. Nython очень интересный язык программирования"
# str2 = chang_char_to_str(str1, "N", "P")
# print(str1)
# print(str2)

# print(u"Привет")
# print("Привет")

# print("C\\file.txt")
# print(r"C\file.txt")
# print(r"C\file.txt\\"[:-1])
# print(r"C\file.txt" + "\\")

# 11.03.

# dom

# def avg(fn):
#     def wrap(*args):
#         st = ""
#         for i in args:
#             st += str(i) + ", "
#         print("Среднее арифметическое:", st[:-2], "=", fn(*args) / len(args))
#
#     return wrap
#
# @avg
# def summa(*args):
#     print("Сумма чисел:", *args, "=", sum(args))
#     return sum(args)
#
# summa(2, 3, 3, 4)

# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# x = 10
# y = 5
# print(f"{x=}, {y=}")
#
# print(f"{x} x {y} / 2 = {round(x * y / 7,2)}")
# print(f"{x} x {y} / 7 = {x * y / 7:3f}")

# num = 74
# print(f"{{{num}}}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")

# s = ("Однострочный "
#       "текст")
# print(s)
#
# s1 = ("Однострочный "
#       "текст")
# print(s1)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n ** 2
#     return res
#
# print(square(5))
# print(square.__doc__)
# print(len.__doc__)
# print(min.__doc__)
# print(max.__doc__)
# print(sum.__doc__)

# from math import pi
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('п'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифмитическое:", arr)
# arr += [ord(x) for x in input("->")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) -1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))
# print(chr(11057))

# a = 122
# b = 97
# if a > b:
#     for i in range(b, a +1):
#         print(chr(i), end=" ")
#     else:
#         for i in range(a, b, + 1):
#             print(chr(i), end=" ")

# from random import randint
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
# print("Случайный пароль:", random_password())

# print(dir(str))

# s = "hello, WORLD! I am learning Python"
# print(s.capitalize())# Hello, world! i am learning python
# print(s.lower())# hello, world! i am learning python
# print(s.upper())# HELLO, WORLD! I AM LEARNING PYTHON

# print(s.count("h", 1, -4))
# print(s.lower().count("i"))

# print(s.find("Python"))
# print(s.find("h", 1, -4))
# print(s.find("h"))
# print(s.rfind("h"))
# print(s.index("h"))
# print(s.rindex("h"))


# st = "один два"
# one = st[:st.find(" ")]# st[:4]
# two = st[st.find(" ") + 1:]# st[4:]
# res = two + " " + one
# print(res)
#
# st = "один два"
# print(st[st.find(" ") + 1:] + " " + st[:st.find(" ")])

# s = "hello, WORLD! I am learning Python"
# print(s.startswith("hello"))
# print(s.startswith("I am", 14))
# print(s.find("I am"))
#
# print(s.endswith("Pyton."))

# print("abc123".isalnum())# СОСТОИТ ЛИ СТРОКА ИЗ БУКВ И ЦИФР

# print("ABCabcП".isalpha()) # состоит ли строка из букв

# print("123".isdigit())# состоит ли строка из цифр

# print('aab'.islower()) # находяться ли в строке буквы в ижнем регистре допускаеться наличие других симолов

# print("ABC".isupper())# находяться ли в строке буквы вверхнем регистре допускаються другие символы

# print("py".center(10, "-"))# выравнивание по центру

# print("    py".lstrip())
# print("py    ".rstrip())
# print("    py    ".strip())
#
# print("https://www.python.org".lstrip("/:htps"))
# print("https://www.python.org.www".lstrip("/:htps").rstrip(".w"))
# print("https://www.python.org.www".strip("/:htps.w"))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("Nython", "Python", 2))


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '99']))
#
# print(":".join("Hello"))


s = "Hello"
print(s[::-1])








