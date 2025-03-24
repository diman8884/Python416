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

# s = "Hello"
# print(s[::-1])

# 13.03.
#
# dom

# s = " I am learning Python. hello, WORLD!"
# a = s[:s.find('h')] #s[:17]
# b = s[s.find('h'):s.rfind('h') + 1]# s[17:23] # hon.h
# c = s[s.rfind('h') + 1:] # s[23:]
#
# print(a + b[::-1] + c)


# print("Строка разделенная пробелами".split())
# print("www.python.org".split('.'))
# print("www.python.org".split('.', 1))

# s = input("Введите ФИО:").split()
# print(s)
# print(f"{s[0]} {s[1][0]}. {s[2][0]}.")

# s = input("Введите числа через пробел: ").split()
# print(s)
# num = list(map(int, s))
# print(num)
# print(sum(num))

# Регулятор выражения

# import re

# s ="Я ищу совпадения в 2025 году. И я их найду в 2 счета."
# reg = r"\." #"[яи]" #"я"
# print(re.findall(reg, s)) # возвращает список совпадения с шаблона
# print(re.search(reg, s)) # возвращает только первое совпадение с шаблона
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).span())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.split(reg, s)) # возвращает список, который разбит по заданному шаблону
# print(re.sub(reg, "!", s)) # поиск и замена

# s ="Я ищу совпадения в 2025 году. И я их найду в 2 счета. 6789. [Hel_lo] World"
# # reg = r"[2025]"
# # reg = r"[12][0-9][0-9][0-9]"
# # reg = r"[a-яА-Я]"
# # reg = r"[А-яЁё].\[\]]"
# # reg = r"[A-Za-z]"
# reg = r"[^0-9]"
# print(re.findall(reg, s))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15t21:45. Минуты, в диапазоне от 00 до 59Ю 2021-06-15T01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счета. 6789. [Hel_lo] World"
# reg =r"/d" # [0-9]
# reg = r"\d" # [^0-9)
# reg = r"s" # []
# reg = r"\w" # [a-яА-Za-z0-9]
# reg = r"\W" # [^A-яА-Za-z0-9]
# reg = r"Wor-ld\Z"
# reg = r"\Вния"
# reg = r"\w+"
# reg = r"\w+"
# reg = r"20*"
# print(re.findall(reg, s))

# Колличество повторений
# + -от 1 до бесконечности
# * -от 0 до бесконечности
# ? -от 0 до 1 бесконечности

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# # reg =r'\d+'
# # reg = r"[+-]?\d+"
# reg = r"[+-]?[\d.]+"
# print(re.findall(reg, d))

# st = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s", "", st))
# print(re.sub("-", ".", st))
#
# print("Дата рождения:", re.sub(r"\s#.+", "", re.sub("-", ".", st)))

# st = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w*\s*\w*.?\w*\.?"
# # reg = r"\w+\s*=\s*\w+[\s\w.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
# print(re.split(r";\s", st))

# st = "12 сентября 2025 год"
# # reg = r"\d{4}"
# #reg = r"/d{2,4}
# # reg = r"\d{,4}"
# # reg = r"\d{4,}"
# print(re.findall(reg, st))

# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счета. 6789. [Hel_lo] Wor-ld 20000000"
# reg = r"\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))

# import re
#
# def validate_login(login):
#     return re.findall(r"^$[a-zA-Z0-9_-]{3,16]", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("Pyt"))
# print(validate_login("$Pyt"))

