# анонимные функции (lambda - выражения)
# from curses import wrapper


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

#06.03

# dom

# from math import pi
#
# area = {
#     'Cicle': lambda x: pi * x *x,
#     'Rectangle': lambda x, y: x * y,
#     'Trapezoid': lambda a, b, h: (a + b) * h / 2
# }
#
# print(area['Circle'](2))
# print(area['Rectangle'](10, 13))
# print(area['Trapezoid'](7, 5, 3))

#Декораторы

# def my_decorator(func):    def func_wrapper():        print("Код до функции")        func()        print("Код после функции")            return func_wrapperdef func_test():    print("Hello, I am func 'func_test'")        test = my_decorator(func_test)test()
def bold(fn):
    def wrap():
        return "<b>" + fn() + "</b"

    return wrap

#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i"
#
#     return wrap
#
# @italic
# @bold
# def hello():
#     return "text"
#
# print(hello())

# def cnt(fn):
#     count = 0
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
# @cnt
# def hello():
#     print("hello")

# hello()
# hello()
# hello()

# def outer(fn):
#     def inner(args1, args2):
#         print("Данные:", args1, args2)
#         fn(args1, args2)
#     return inner
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
# print_full_name("Ирина", "Ветрова")

# def outer(fn):
#     def inner(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#     return inner
# @outer
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "изучают:", study, end="\n\n")
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x,y)
#         return wrap
#     return args_dec
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
# summa(5, 2)
# sub(15, 12)



# def multiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             print(*args)
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return my_decorator
#
# @multiply(3)
# def return_num(*num):
#     return num
#
#
# print("Результат:", return_num(5))

# Строки

# print(bin(18)) #0b10010-двоичная система счисления
# print(oct(18)) # 0o22- восьмеричная система счисления
# print(hex(18))  #0x12 - шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010 + 4)

# unicode

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print("y" in e)
# print("a" in e)
# print(e[1])
# print(e[-1])
# print(e[1:3])

# def chang_char_to_str(s, old, new):
#     s2 = "" #"Я изучаю P ............P .........P"
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
# str1 = "Я изучаю Nython. Мне нравиться Nython. Nython очень интересный язык программирования"
# str2 = chang_char_to_str(str1, "N", "P")
# print(str1)
# print(str2)

# print(u"Привет")
# print("Привет")

print("C\\file.txt")
print(r"C\file.txt")
print(r"C\file.txt\\"[:-1])
print(r"C\file.txt" + "\\")