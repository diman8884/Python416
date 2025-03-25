

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

#18 03

# import re

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
#
# text = "hello world"
# print(re.findall(r"\w+", text))
# print(re.findall(r"\w\+", text, re.DEBUG))


# text = "heLlo world"
# print(re.findall(r"L", text, re.IGNORECASE))

# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))

# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""[a-z, -]+@[a-z.]+""", "test@mail.ru"))

# print(re.findall("""
# [a-z, -]+ # part 1
# @         # @
# [a-z.]+   # part 2
# """, "test@mail.ru", re.VERBOSE))

# text = """Python<
# python
# PYTHON
# """
#
# reg = "(?im)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# *?, +?, ??
#{m,n}?, {,n}?, {m,}

# s = "Петр, Ольга т Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Василий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.of, double = 8.0"
# # reg = r"int\s*=\s*\d[\w.]*|float\s*=\s*\d[\w.]*"
# reg = r"(?:int|float)\s*=\s*\d[\w.]*"
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# # reg = r"([a-z]+)\d+"
# # reg = r"[a-z]+(\d+)"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))

# s = "5 + 7*2 - 4"
# # reg = r"\s*[+*-]\s*"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# s = '28-08-2021' #01 - 31
# reg = r"([0][1-9]|[12][0-9]|[3][01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# # print(re.split(reg, s))

import re

# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))
# m = re.search(reg, s, re.IGNORECAS)

# s= "Самолет прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025"
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))

# рекурсия

# def elevator(n): # 3
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n -1) # стек 5 4
#     print(n, end=" ")
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
# print(sum_list([1, 3, 5, 7, 9]))
#
# def sum_list(lst):# {1, 3, 5, 7, 9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:]) # 1 + 3 + 5 + 7 +9
# print(sum_list([1, 3, 5, 7, 9])) # 25

# def to_str(n, base): # n = 254, base = 16
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n] # 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base] # 'F' + 'E'
# print(to_str(254, 16))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#     else:
#         count += 1
#     return count
#
# print(count_items(names))