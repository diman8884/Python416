# методы словарей

# d = {"A": 1, "B": 2, "C": 3}
#
# print(d)
#
# print(d.keys())# список ключей
# print(d.values())# список значений
# print(d.items())# список ключей и значение в виде кортежа
#
# for i, j in d.items():
#     print(i, ":", j)
# print(d)

# d = {"A": 1, "B": 2, "C": 3}
# d2 = d.copy() # возвращается копия словаря
# print("D =", d )
# print("D2 =", d2)
# d2["B"] = 5
# print("D =", d )
# print("D2 =", d2)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # d.clear()# удаляет все элементы словаря
# #item = d.pop("B", "Такого ключа не существует в словаре")# удаляем элемент по ключу
# item = d.popitem() # удаляет последний элемент и возвращает кортеж из ключа и значения
# print(d)
# print(item)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# #print(d[B])
# value = d.get("B" "Такого ключа не существует в словаре") #"W" # получает значение по заданному ключу
# print(value)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# d["B"] = 10
# item = d.setdefault("M", 5)# по заданному ключу добавляет новый ключ и значение, а если ключа не существовало
# print(d)
# print(item)

# d = {"A": 1, "B": 2, "C": 3}
# # d2 = {"R": 7, "Q": 9, "B": 5}
# d2 = [("R"," 7"), ("Q", 9)]
# print(d)
# print(d2)
# # d3 = d | d2
# d.update(d2)
# print(d)

# d= {"name": "Kelly", "Age": 25, "salary": 8000, "city": "New york"}
#
# new_d = dict()
# # new_d["name"] = d.pop("name")
# # new_d["salary"] = d.pop("salary")
# new_d["name"], new_d["salary"] = d.pop("name"), d.pop("salary")
# print(d)
# print(new_d)

# d= {"name": "Kelly", "Age": 25, "salary": 8000, "city": "New york"}
# d['location'] = d.pop("city")
# print(d)

# d = {
#     "first":{
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "second":{
#         4: "four",
#         5: "five"
#     }
# }
# print(d)
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ": ", d[x][y], sep="")

# 25.02

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print({v: k for k, v in d.items()})

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print({k: v for k, v in d.items() if v <= 2})

# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# d1 = {i: i * 3 for i in s}
# print(d1)

# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, 'four', -20]
# d = dict() # {"one": [1, 2, 3]}
# s = None
#
# for i in lst: # 1, 2, 3
#     if type(i) == str:
#         d[i] = []
#         s = i # s ='one'
#     else:
#         d[s].append(i)
#
# print(d)

# zip([], [])

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# d1 = list(zip([1, 2, 3], ['one', 'two', 'three'], [True, False, True]))# объединяет несколько последовательностей в одну
# print(d1

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = {k: v for k, v in zip(a, b)}
# print(d)

# a = [1, 2, 3]
# c = list(zip(a))
# print(c)

# one = {"name": "Igor", "surname": "Pavlov", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Trove", "job": "Manager"}
#
# for (k1,v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# lst = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*lst)
# print(a)
# print(b)

# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 1, 2]
# d = dict(zip(letter, number))
# print(d)
#
# data1 = list(zip(letter, number))
# print(data1)
# data1.sort()
# print(data1)
#
# d2 = dict(data1)
# print(d2)

# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 1, 2]
# d = dict(zip(letter, number))
# print(d)
#
# data = sorted(d.items())
# print(data)

# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# print(b)

# one = {"один": 1, "два": 2}
# two = {"три": 3, "четыре": 4}
# print({**one, **two})

# colors = ["red", "yellow", "green"]
# i = 1
# for color in colors:
#     print(i, ")", color, sep="")
#     i += 1
# print()
# for j, color in enumerate(colors, 1):
#     print(j, ")", color, sep="")

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ")", k, ": ", v, sep="")

# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3))
# print(func())

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))

# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))

# def func(a, b, *args):
#     return a, b, args
#
# print(func(5, 6))
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))