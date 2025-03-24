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

# 27.02

# def func1(*args):
#     print("args:", args)
#     print(args[0])
#
# def func2(**kwargs):
#     print("kwargs:", kwargs)
#     print(kwargs["one"])
#
# func1(1, 2, 3, 4, 5, 6)
# func2(one=123, two=456)

#Область видимости(scape)

# name = "Tom" # глобальная переменная
#
#
# def hi():
#     global name # делаем глобальную переменную
#     name = "San"
#     surname = "Jonson" # локальная переменная
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
# # print(name)
# hi()
# bye()
# print(name)

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# # print_ = 5
#
# lst =[9, 8, 7, 6, 4, 3, 2, 1]
# print(sum(lst))

# x = 4
#
# def func():
#     x = 2 # вызов 2
#
#     def inner():
#         print("x =", x) # вызов 4
#         print(x + 3)
#     # print(x) # вызов 5
#     inner()# вызов 3
# func() # вызов 1

# вложенная функции

# def outer(a):
#     def inner():
#         print("Hello", a)
#
#     inner()
#
# outer("World")

# def fun1():
#     a = 6 # вызов 2
#
#     def fun2(b):
#         a = 4 # вызов 5
#         print("Сумма: ", a + b) # вызов 6
#
#     print("a:", a) # вызов 3
#     fun2(3) # вызов 4
#
# fun1() # вызов 1

# x = 25
#
# def fn():
#     global t
#     a = 30
#     t = a
#
# fn()
# c = x + t # 25 + 30 = 55
# print(c)

# x = 25
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#     a= 35
#     print("a =", a)
#
#     inner()
#     t = a
#
# fn()
# c = x + t # 25 + 30 = 55 # 25 + 35 = 60
# print(c)

# def fn1():
#     x =25 # 55
#
#     def fn2():
#         x = 33 # 55
#
#         def fn3():
#             x = 55
#
#         fn3()
#         print("fn2.x =", x) # 33 -> 55
#
#     fn2()
#     print("fn.x =", x) # 25
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return[a, b]
#
# print(outer(2, 3, -1, 4))# [1,7]

# дом

# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
# func1 = outer(5)
# print(func1(10))
#
# func2 = outer(6)
# print(func2(10))

# def func1():
#     a = 1
#     b = "Line"
#     c = [1, 2, 3]
#     def func2():
#         nonlocal a, b
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#     return func2
# func = func1()
# print(func())

def func(city):
    n = 0 # 1 # 2 # 3
    def inner():
        nonlocal  n
        n += 1
        print(city, n)

    return inner

res1 = func("Москва")
res1()
res1()
res2 = func("Сочи")
res2()
res2()

res1()
res1()