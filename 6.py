#[выражение  for переменная in последовательность]

# a = [0 for _ in range(5)] # 0 1 2 3 4 5
# print(a) #[0 0 0 0 0]


# a = ["*" for _ in range(5)] # 0 1 2 3 4 5
# print(a) #[0 0 0 0 0]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a) #[1, 4,9, 16]

# a = [0] * int(input("Введите колличество элеменов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("->") for i in range(int(input("n = ")))]
# print(a)

# a = list(range(10, 100, 10))
# print(a)
# for i in range(len(a)): # 0 1 2 3 4 5 6 7 8
#     # print(i, end=" ")
#     print(a[i] + 2, end=" ")
# print()
# for i in a:
#     print(i + 2, end=" ")

# a = [int(input("->")) for i in range(int(input("n = ")))]
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма отрицатeльных элементов:", s)

# a = [int(input("->")) for _ in range(int(input("n = ")))]
# s = 0
# i = 0
# while i < len(a):
#     if a[i] < 0:
#         s += a[i]
#     i += 1
# print("Сумма отрицатeльных элементов:", s)

# a = [int(input("->")) for _ in range(int(input("n = ")))]
# s = 0
# for v in a:
#     if v < 0:
#         s += v
# print("Сумма отрицатeльных элементов:", s)

# a = [int(input("->")) for _ in range(int(input("n = ")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
# print()
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input("->")) for _ in range(int(input("n = ")))]
# print(a)
#
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [int(input("-> ")) for _ in range(int(input("n = ")))]
# print(a)
# for i in a:
#     if i > i -1:
#         print(i, end=" ")

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)): #range(0, len(a), 1)
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Колличество четных элементов:", k)
# print("Сумма нечетных элементов:", s)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("Колличество четных элементов:", k)
# print("Сумма нечетных элементов:", s)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("Сумма арифмитическое:", s)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# sum1 = kol = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         sum1 += a[i]
#         kol += 1print("среднее арифметическое", sum1/kol)

# lst = [7, 9, 2, 1, 27]
# print(lst)
# lst[0], lst[1] = lst[1], lst [0]
# print(lst)

#срез
# список[start: stop:step]

# s = [9, 7, 2, 1, 17, 8]
# print(s)
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[::3])
# print(s[::-1])
# print(s[::])
# print(s[:])
# print(s[0:-1])
# print(s[1:-1])
# print(s[-1:0:-1])
# print(s[10:-20])

# lst =  list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:7])
# print(lst[4:])
# print(lst[2:5])

# st = "Hello World"
# print(st[1:3])
# print(st[::-1])

# st = "123456"
# print(st[1:3])
# num = st[::-1]
# print(num)
# print(type(num))
# num = int(num)
# print(num)
# print(type(num))

# lst = list(range(1,8))
# print(lst)
# lst[1:3] = [0, 0, 0, 0]
# print(lst)
# lst[1:2] = [20]
# print(lst)
# lst[1:2] = [40, 8, 2]
# print(lst)
# lst[3] = [40, 8, 2]
# print(lst)
# lst[15:16] = [100]
# print(lst)
# print(len(lst))

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

a = [5, 9, 2, 1, 4, 3, 4, 2]
b = [4, 2, 1, 3, 7, 2]
c = []
for element in a:
    if element not in c: # добавляються элементы из первого списка без повторения
    # if element not in c and element in b: #c[5,9,2,1,4,3] b[2,1,4,3,4,2] при использовании с и в убираем дубликаты
        c.append(element)
print(c)
