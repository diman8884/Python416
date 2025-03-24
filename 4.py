# n = int(input("Введите число от 1 до 99: "))
# num = n
# if 11 <= num <= 14:
#     print(n, "копеек")
# elif 1 <= n <= 99:
#     num = num % 10
#     if num == 1:
#         print(n, "копейка")
#     elif 2 <= num <= 4:
#         print(n, "копейки")
#     else:
#         print(n, "копеек")
# else:
#     print("Значение должно быть от 1 до 99: ")

# тернарное выражение
#a, b = 10, 20
#print(a if a < b else b)

# res = 0
# a, b = 30, 20
# print("На 0 делить нельзя" if b == 0 else a / b)

# Исключения

# a = 5
# b = 0
# print(a / b)

# try: #gjgsnfnmcz
#     n = int(input("Введите целое число:"))
#     print(n * 2)
# except ValueError: # except исключение
#     print("Что-то пошло не так")
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делимое: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на 0")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делимое: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на 0")
# else: # когда в блоке try  не возникло исключения
#     print("Все нормально. Вы ввели", n, "и", m)
# finally: # выполниться в любом случае
#     print(" Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#    n = int(n) # n = 5
#    m = int(m) # m = "qqqq"
# except ValueError:
#     n = str(n) # n = "5"
#     m = str(m)
# finally:
#     print(n + m)

# Циклы

# while  условие:
#     блок кода

# итерация  - один шаг цикла

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# print()

# j = 2
# while j <= 20:
#     print(j, end = " ")
#     j += 2

# n = int(input("Укажите колличество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите колличество символов: "))
# print("*" * n)

# a = int(input("Введите начало диапозона: "))
# b = int(input("Введите конец диапозона: "))
# res = 0
# while a <= b:
#     if a % 2: # 1 3 5
#         res += a
#     a += 1
# print("Сумма нечетныз чисел:", res)

# n = input("Введите целое число:")
# while type(n) != int:# != int или is not = int
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#           i += 1
#           continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\n Цикл окончен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# res = 1
# while True:
#     n = int(input("Введите цисло: "))
#     if n == 0:
#         break
#     res += n
# print(res)

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1




