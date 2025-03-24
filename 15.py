# вложенная функции
from types import LambdaType

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

# def func(city):
#     n = 0 # 1 # 2 # 3
#     def inner():
#         nonlocal  n
#         n += 1
#         print(city, n)
#
#     return inner
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
#
# res1()
# res1()

# 04.03.25

# анонимные функции (lambda - выражения)

# def func(x, y):
#     return x + y
#
# print (func(1, 2))
# print((lambda x, y: x + y)(1, 2))
#
# func = lambda  x, y: x + y
# print(func(1, 2))
#
# func = (lambda x, y: x + y)(1, 2)
# print(func)

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())

# print((lambda *args: sum(args))(1, 2, 3, 4))

# tpl = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in tpl:
#     print(t("abc___"))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# f = outer(42)
# print(f(3))
#
# def outer(n):
#     return lambda  x: n + x
# f = outer(42)
# print(f(3))
#
# outer = lambda  n: lambda x: n + x
# f = outer(42)
# print(f(3))
#
# print((lambda n: lambda x: n + x)(42)(3))

# print ((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))

# def func(i):
#     return i[1]
#
# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)
# print(dict(lst))

# players =[
#     {'name': 'Антон', 'Last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'Last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'Last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'Last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda i: i['Last name'])
# print(res)
#
# res = sorted(players, key=lambda i: i['rating'], reverse=True)
# print(res)
#
# res = sorted(players, key=lambda i: i['rating'])
# print(res)

# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(lst[0](12, 6))
# print(lst[1](12, 6))
# print(lst[2](12, 6))
# print(lst[3](12, 6))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
# d[2]()
# d[5]()

# from random import randint
# s = (lambda lst: [randint(10, 20) for i in range(10)])([])
#
# print((lambda lst: [i * 2 for i in lst])([1, 2, 3, 4, 5, 6]))

# map(function, iterables), filter(function, iterables)

# def mult(t):
#     return t * 2
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
# print(tuple(map(mult, lst)))

# t = (2.88, -1.75, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))
# print(tuple(map(round, t)))
# print(tuple(map(str, t)))

# st = ['a', 'b', 'c', 'd', 'e', 'w']
# num = [1, 2, 3, 4, 5]
#
# print(dict(map(lambda x, y: (x, y), st, num)))
# print(list(map(lambda x, y: (x, y), st, num)))

# st = ['a', 'b', 'c', 'd', 'e', 'w']
# num = [1, 2, 3, 4, 5]
# tpl = (True, False, True, True)
#
# print(set(map(lambda a, b, c: a + str(b) + str(c), st, num, tpl)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda a, b: a + b, l1, l2)))

# lst = [input("->") for i in range(5)]
# print(lst)
# lst = list(map(int, lst))
# print(lst)

# t = ('abcd', 'abc', 'cdefg', 'def', 'gh1')
# print(tuple(filter(lambda s: len(s) == 3, t)))
# print(tuple(filter(lambda s: s * 3, t))) # пример

# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# lst = list(filter(lambda s: s > 75, lst))
# print(lst)

# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
#
# print(list(filter(lambda a: (a >= 10) and a <= 20, lst)))
# print(list(filter(lambda a: 10 <= a <= 20, lst)))

# nums = [45, 55, 60, 37, 100, 105, 220]
#
# print(list(filter(lambda s: s % 15 == 0, nums)))
# print(list(filter(lambda s: not s % 15, nums)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))