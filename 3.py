#print(2 < 4  < 9) # true && true => true
#print(2 * 5 > 7 >= 4 + 3) # 10 > 7 >= 7 true && true => true
#print(3 * 3 <= 7 >= 2) # 9<=7>=2 False && True => False

#a = "10"
#b = 5
#c = a == b
#print(a, b, c)

#print(5 - 3 == 2 and 1 + 3 == 4)# true and true => True
#print(5 - 3 == 2 and 1 + 3 < 4)# true and false => false

#print(5 - 3 == 2 or 1 + 3 == 4)#true or true => true
#print(5 - 3 == 2 or 1 + 3 < 4)#true or false => false

#print(not 9 - 5)#
#print (not 7 - 7)

#a = 5
#print("a:",a)

#print("строка текст")

#cnt = 15 #5
#if cnt < 10:
  #  cnt = cnt + 1
  #  print(cnt)

#age = int(input("Введите свой возраст:"))
#if age >= 18:
#    print("Доступ на сайт разрешен")
#else:
#    print("Доступ запрещен")

#a = 20 # 15
#b = 15
#if a>b:
 #   print("a > b")
#elif a == b:
#        print("a == b")
#else:
 #   print("b > a")

#a = input("Введите первую строку: ")
#b = input("Введите вторую строку: ")
#c = input("Введите третью строку: ")
#if a == b == c:
 #   print("Треугольник равностороний")
#elif a == b or b == c or a == c:
 #   print("Треугольник 2равнобедреный")
#else:
#    print("Треугольник разностороний")

#day = int(input("Введите день недели (цифровой): "))
#if 1<= day <= 5: #(day >= 1) and (day <= 5)
 #   print("Рабочий день - ", end="")
#    if day == 1:
#        print("Понедельник")
 #   if day == 2:
 #       print("Вторник")
  #  if day == 3:
  #      print("Среда")
   # if day == 4:
  #      print("Четверг")
  #  if day == 5:
  #     print("Пятница")
#elif day == 6 or day == 7:
 #   print("Выходной день")
 #   if day == 6:
     #   print("Суббота")
  #  if day == 7:
  #     print("Воскресенье")
#else:
 #   print("Такого дня недели не существует")

#season = int(input("Введите номер месяца: "))
#if 1 <= season <= 12:
#    print("Время года: ", end="")
#    if 1 <= season <= 2 or season == 12:
 #       print("Зима")
 #   if 3 <= season <= 5:
 #       print("Весна")
#    if 6 <= season <= 8:
 #       print("Лето")
 #   if 9 <= season <= 11:
 #       print("Осень")
#else:
 #       print("Такого месяца нет")

#n = int(input("Введите колличество ворон: "))
#if 0 <= n <= 9:
#    print("На ветке ", end="")
#    if n == 1:
 #       print(n, "ворона")
 #   if 2 <= n <= 4:
#        print(n, "вороны")
 #   if 5 <= n <= 9 or n == 0:
 #       print(n, "ворон")
 #   else:
 #     print("Ошибка ввода")

#n = int(input("Введите количество ворон: "))
#if 0 <= n <= 9:
 #   print("На ветке ворон", end="")
 #   if n == 1:
  #      print("а", n)
 #   if 2 <= n <= 4:
  #      print("ы", n)
 #   if 5 <= n <= 9 or n == 0:
 #       print("", n)
 #   else:
 #       print("Ошибка ввода")


#n = int(input("Введите количество ворон: "))
#if 0 <= n <= 9:
#   print("На ветке ворон", end="")
#    if n == 1:
#        print("а", n)
#   elif 2 <= n <= 4:
#      print("ы", n)
#   else:
#       print("", n)
#else:
#      print("Ошибка ввода")

#match выражение:
#   case шаблон 1:
 #       действие 1:
#    case шаблон 2:
 #       действие 2:
 #   case _:
#        значение по умолчанию


#assword = "user" #admin user qwerty
#match password:
 #   case "admin":
 #       print("Администратор")
 #   case "user":
#        print("Пользователь")
#case _:
 #       print("Пароль неверен")

#day = "Понедельник"
#time = 13
#match day:
 #   case "Понедельник" | "Вторник" | "Среда" | "Четверг" | "Пятница" if 9 <= time <= 12 or 14 <= time <= 17:
 #        print("Рабочий день")
 #   case " Суббота" | "Воскресенье":
  #       print("Выходной день")
#    case _:
 #        print("Такого дня недели не существует или не рабочее время")


# тернарное выражение
#a, b = 10, 20
#print(a if a < b else b)

res = 0
a, b = 30, 20
print("На 0 делить нельзя" if b == 0 else a / b)



