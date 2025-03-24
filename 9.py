
# lst = [11, 1, 22, 2, 33, 3, 55, 66, 22]
# lst.remove(22) # удаляет элемент из списка по значению
# print(lst)

# lst = [11, 1, 22, 2, 33, 3, 55, 66,]
# lst.remove(22) # удаляет элемент из списка по значению
# print(lst)
# last = lst.pop() # удаляет последний список элемента из списка и возвращает его
# print(last)
# print(lst)
# second = lst.pop(20) # удаляет последний список элемента из списка и возвращает его если индекса нет то получаем исключение
# print(second)
# print(lst)
# lst.clear()# удаляет все элементы списка
# print(lst)

# print("Введите элементы списка:")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# value = 33# создает копию списка по другому адресу
# if value in lst:
#     ind = lst.index(value, 5, 8) # возвращает индекс первого вхождения мскомого элемента можно указать
#     # диапазон от колкого до кого индекса мы производим поиск может выбрвсыыать исключение валуеэрор
#     # если элемент не найден
#     print(ind)
# print(lst)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# lst.reverse()#развернул элементы списка в противоположную сторону
# print(lst)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# lst.sort(reverse=True)
# print(lst)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key=len, reverse=True)
# print(s)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# st = "Hello"
# new_lst = sorted(st, reverse= True)
# print(new_lst)
# print(st)

# генерация случайных данных
# import random
# print(random.random())
# print(random.randint(5, 10))
# print(random.randrange(5, 10, 2))
# print(random.uniform(10,25.5))

# city_list = ['москва', 'новосибирск', 'воронеж', 'сочи', 'екатеринбург']
# s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 3, 8]
# # print(random.choice(city_list))
# # print(random.choice(s))
# # print(random.choices(city_list, k=3))
# # print(random.choices(s, k=3))
# random.shuffle(city_list)
# random.shuffle(s)
# print(city_list)
# print(s)
#
# import random

# mas1 = [random.randint(0, 100) for i in range(10)]
# print(mas1)
# mas = mas1.copy()
# mas.sort()
# #print(mas)
# min_ = mas[0]
# print("Min = ", min_)
# ind = mas1.index(min_)
# print(ind) # минимальный индекс
# del mas1[:ind]
# print(mas1)

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(len(mas))# длина списка
# print(min(mas)) # минимальный элемент
# print(max(mas)) # максимальный элемент
# print(sum(mas)) # сумма элемента списка
# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# maximum = max(mas)
# print("max =", maximum)
# mas.remove(maximum)
# print(mas)
# mas.insert(0, maximum)
# print(mas)

# import random
# mas = [random.randint(0, 10) for i in range(10)]
# print(mas)
# print(2 not in mas)

# lst =[5]
# # if len(lst) == 0:
# #     print("Список пустой")
# print(bool(lst))
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")

m = [
    [1, 2, 3, 4], # 0
    [5, 6, 7, 8], # 1
    [9, 10, 11, 12] # 2
]
# print(m)
# print(len(m))
# print(m[1][2])
# print(m[2][1])
# print(m[1][3])

# print("Вариант 1")
# for row in range(len(m)): #row = 0 # 0 1 2
#     # print(m[row])
#     for col in range(len(m[row])): #0 1 2 3
#         print(m[row] [col], end="\t")
#     print()
# print("Вариант 2")
# for i in m:
#     for j in i:
#         print(j, end="\t")
#     print()

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

import time

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





