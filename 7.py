# методы списков

# lst = list(range(1,8))
# print(lst)
# lst.append(99) # добавляет один элемент в конец списка
# print(lst)
# lst.extend([1,2,3]) # добавляет список элементов в конец списка
# print(lst)
# lst.insert(0, 100) #  добавляет элемент в указанный индекс перезаписывая номера остальных индексы назад
# print(lst)

# s = []
# n = int(input("Колличество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x) #123
#     s.insert(0, x) # 321
# print(s)

# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 3, 7, 2]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue # если число уже есть в списке то ее не добавляем тоесть избегаем дублеката
#         if i == j: #5(a) == 4(b) 9(a) == 2(b и тд) 9(a) == 4(b) 5(a) == 2(b и тд) и так по кругу
#             c.append(i)
#             break # когда дошел до первого совпадения начинате искать следуещее тоесть 2=2 стоп 1=1 стоп и  т.д
# print(c)

# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 3, 7, 2]
# c = []
# for element in a:
#     if element not in c: # добавляються элементы из первого списка без повторения
#     # if element not in c and element in b: #c[5,9,2,1,4,3] b[2,1,4,3,4,2] при использовании с и в убираем дубликаты
#         c.append(element)
# print(c)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)

# домашка

# lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# new_lst = []
# i = 0
# for element in lst:
#     k = element # 5
#     for j in lst:# 1
#         if k == j:# 3==3
#             i += 1# i = 1
#     if i == 1:
#         new_lst.append(k) # 3
#     i = 0
# print(new_lst)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         b.append(a[i]) #3, 5, 4, 7
# print(b)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# for i in a:#3 5 6
#     if a.count(i) == 1:# 1=1 5=1 4=1 7=1
#        print(i, end="")#3 5 4 7

# a = [1,2,3]
# b = [11,22, 33, 4, 2]
# c = []
# for i in range(len(a)): # 0 1 2
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# a = [1, 2, 3,]
# b = [11,22, 33, 55, 66]
# c = []
# for i in range(len(a)): # 0 1 2
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# lst = [11, 1, 22, 33, 3, 55, 66]
# lst[5:] = []
# print(lst)

# lst = [11, 1, 22, 33, 3, 55, 66]
# lst[3:5] = []
# print(lst)

# lst = [11, 1, 22, 33, 3, 55, 66]
# lst[:] = []
# print(lst)

# lst = [11, 1, 22, 33, 3, 55, 66]
# del lst[2]
# print(lst)

# lst = [11, 1, 22, 2, 33, 3, 55, 66]
# del lst[2:7]
# print(lst)

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
#     # диапозон от кокого до кого индекса мы производим поиск может выбрвсыыать исключение валуеэрор
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
import random
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

import random

mas = [random.randint(0,100) for i in range(10)]
print(mas)