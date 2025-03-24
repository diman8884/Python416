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
#
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

#13

# def func(a, b=0):
#     return a + b
#
# print(func(2, 5))
# print(func(2, 5))
# print(func(2))

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)
#
# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)


# lst1= [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))

# a = "hello"
# print(a, id(a))
# a = a + "!"
# print(a, id(a))

# a = 5
# print(a, id(a))
# a = a + 3
# print(a, id(a))

#Картеж (кортеж)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# print(lst[1])
# print(tpl[1])
#
# lst[1] = 50
# print(lst)

# a = 1, 2, 3, 4, 5
# print(a, type(a))
# a = (1, 2, 3, 4, 5)
# print(a, type(a))
# a = ()
# print(a, type(a))

# a = list("Hello")
# print(a, type(a))
# a = tuple("Hello")
# print(a, type(a))

# a = 1, 2, 3, 4, 5
# print(a[2])
# print(a[1:3])

# print([i for i in range (10)])
# print(tuple(i for i in range (10)))
# print(tuple([i for i in range (10)]))
# from random import randint
# print(tuple(i + 2 for i in range(10)))
# print(tuple(input("->") for i in range(5)))

# print(tuple(randint(50, 100) for i in range(10)))

# t1 = tuple("Hello")
# t2 = tuple("world")
# t3 = t1 + t2
# # print(t3 * 2)
# print(t3)
# # print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# # print(t3.index("l", 9))
# if 'a' in t3:
#     print(t3. index("e"))
# else:
#     print("Такого элемента нет")

# for i in t3:
#     print(i, end="")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):] #tpl[2:]
#         else:
#             first = tpl.index(el) # tpl [2:]
#             second = tpl.index(el, first + 1) + 1 # 5
#             print("first", first)
#             print("second", second)
#             return tpl[first:second + 1] # tpl[1:4 + 1] #
#     else:
#         return ()

# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (True, 11, "Python", (4, 5, 6), ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# распаковка кортежа

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# # x, y, z = t
#
# x, y, z = 1, 2 , 3
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# user = get_user()
# print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # frist_name, year, marriend = user
# frist_name, year, marriend = get_user()
# print(frist_name)
# print(year)
# print(marriend)

# lst = [1, 2, 3, 4, 5]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)(
# print(lst2, type(lst2))
# lst2.append(6)
# tpl2 = tuple(lst2)
# # print(tpl2, type(tpl2))
#
# countries =(
#     ("Германия", 80.2, (("Берлин", 3.3326), ("Гамбургер", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# # print(countries)
# for country in countries:
#    country_name, country_population, cities = country
#    print("\nСтрана: ",country_name, ", население = ", country_population, sep="")
#    for city in cities:
#        city_name, city_population = city
#        print("\tГород: ", city_name, ", население = ", city_population, sep="")

tpl = tuple(input("Введите строку: "))
print(tpl)

lst = []
for i in range(len(tpl)):
    if tpl[i] not in lst:
        lst.append(tpl[i])

print(lst)
for i in range(len(lst)):
    print("Колличество", lst[i], "=", tpl.count(lst[i]))