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

# d = {i: i ** 2 for i in range(1, 8)}
# print(d)
# print(3 in  d)# проверяет наличие ключа в словаре
# print(25 in d)
# key = 9
# # if key in d:
# #     del d[key]
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     print(key, ":", d[key])
# for key in d:
#     res *= d[key]
# print(res)

# d =dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)

# d = {i: input("->") for i in range(1,5)}
# print(d)

# d={i: input("->") for i in range(1,5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1':['Core-i3-4300', 9, 4500],
#     '2':['Core-i5-4670', 3, 8500],
#     '3':['AMD FX-6300', 6, 3700],
#     '4':['Pentium G3220',8, 2100],
#     '5':['Core-i5-3450', 5, 6400],
# }
# for i in goods:
#     print(i, ")", goods[i][0], "-", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                   count = int(input("Колличество: "))
#                   goods[n][1] += count
#                   break
#                 except ValueError:
#                    print("Значение некорректное. Введите число")
#         else:
#             print("Такого ключа не существует")
# for i in goods:
#     print(i, ")", goods[i][0], "-", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

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