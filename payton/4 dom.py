
n = int(input("Укажите колличество символов: "))

s = input("Укажите тип символа: ")

w =int(input("Укажите орентирование строки: "))

print("Колличество символов:", n)
print("Тип символа: ", s)
print("0 - орентирование по горизонтали")
print("1 - орентирование по вертикали")

i = 0
if w == 0:
 while i < n:
    print(s, end="")
    i += 1
if w == 1:
 while i < n:
    print(s, "")
    i += 1

# count = input("Укажите кол-во символов: ")
# while type(count) is not int:
#     try:
#         count = int(count)
#         except ValueError:
#         print("Введите целое число")
#         count = input("Введите целое число: ")
#         types = input("Укажите Вид символа: ")
#         orient = input("Укажите направление, 0 - по вертикале, 1 -по горизонтали: ")
#         i = 0
#         while i <= count:
#             if orient == 1:
#                 print(types, end=" ")
#                 if orient == 0:
#                     print(types, end="\n")
#                     i += 1
#                     while type(orient)
#                         is not int:
#                         i = 0
#                         try:
#                             orient = int(orient)
#                             if orient == 0 or orient == 1:
#                                 pass
#                                 else:
#                                 print("Неверное направление!")
#                                 orient = input("Введите направление 1 или 0: ")
#                                 except ValueError:
#                                 print("Неверное направление!")
#                                 orient = input("Введите направление 1 или 0: ")
#                                 i += 1