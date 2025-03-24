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

# tpl = tuple(input("Введите строку: "))
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# print(lst)
# for i in range(len(lst)):
#     print("Колличество", lst[i], "=", tpl.count(lst[i]))

# множество / set

# s = {"red", "yellow", "green", "yellow", "green"}
# print(s)
# print(type(s))
# print(len(s))

# a = set("hello")
# print(a, type(a))

# s = { i for i in range(10)}
# print(s)

# s = { i * i for i in range(10)}
# print(s)

# lst ={10, 2, 2, 2, 2, 3, 3, 8, 9, 9, 9, 10}
# print(lst)
# # st = {i for i in lst if i % 2 == 0 }
# # print(st)
# st = set(lst)
# # print(st)
# lst2 = list(st)
# # print(lst2)

# t = {"red", "yellow", "green"}
# print("green" in t)
# print("blue" in t)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print({i for i in lst if 'a' in i})
# print(tuple("A" if i[0] == "a" else "B" for i in lst))

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print({i for i in lst if 'a' in i})
# print(tuple("A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst))
# print(["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"])
#
# lst2 = []
# for i in lst:
#     if i[1] == "c":
#         if i[0] == "a":
#             lst2.append("A" + i[1:])
#             else:
#             lst2.append("B" + i[1:])
#
# print(lst2)

# print(dir(set))
#
# a = {"red", "yellow", "green"}
# print(a)
# a.add("black") # добавление элемента
# print(a)

# a.remove('yellow') # удаляет элемент
# print(a)
#
# a.remove('blue') #KeyError
# print(a)
#
# el = "green"
# if el in a:
#     a.remove(el)
#
# print(a)

# a = {"red", "yellow", "green"}
# print(a)
# a.discard('blue')# удаляет po значение
# print(a)
#
# a.pop()# удаляет первый элемент из множества
# print(a)
# a.clear() # очистит множество

# a = {0, 1, 2, 3}
# b = {4, 2, 3, 1}
# c = a.union(b) # {0, 1, 2, 3, 4}
# c = a | b
# # print(c)
# a |= b
# print(a)
# c = a & b
# print(c)
# a &= b
# print(a)
# c = a - b
# print(c)
# a -= b
# print(a)
# a = a ^ b
# print(a) #{0, 4}
# # += -=
# a ^= b
# print(a) #{0, 4}
# += -=

# s1 = {1,2}
# # s2 = {3}
# # s3 = {4, 5}
# # s4 = {3, 2, 6}
# # s5 = {6}
# # s6 = {7, 8}
# # s7 = {9, 8}
# #
# # # s = s1 | s2 | s3| s4 | s5 | s6| s7
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# # print(s)
# # print("Кол-во уникальных элементов:", len(s))
# # print("Min:", min(s))
# # print("Max:", max(s))
#
# s1 ="Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# s1 ="Hello"
# s2 = "How are you"
# s1 = set(s1)
# print(s1)
# s2 = set(s2)
# a = s1 & s2
# print(a)
# for i in a:
#     print(i, end=" ")
# print()
# print("s1 =" , s1)
# print("s2 =" , s2)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a <= b
# print(c)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# a = frozenset({"hello", "world"})
# print(a)

# словарь (dict)

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
# print(lst[1])
# print(d["second"])
# print(lst[1])
# lst[1] = "ten"
# print(lst)
# d["second"] = "ten"
# print(d)

# d = {}
# print(d)
# print(type(d))

# d = dict(a="Hello", b="World")
# print(d)
# print(type(d))
#
# d1 = {"a": "Hello", "b": "World"}
# print(d1)

# d = {0: "text", "one": 45, (1, 2):"Кортеж", 42: [9, 8], True: 1, False: 0, "a": "Кортеж", 1: "один", "a": 56}
# print(d)

# user = [
#     ["a", 1],
#     ["b", 2],
#     ["c", 3],
# ]
# print(user)
# new_dict = dict(user)
# print(new_dict)