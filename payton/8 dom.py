import math

shape = int(input("Выбор фигуры:\n1-треугольник\n2-прямоугольник\n3-круг\n: "))
s = None
if shape == 1:
    a = int(input("Введите сторону треугольникa A = "))
    b = int(input("Введите сторону треугольникa B = "))
    c = int(input("Введите сторону треугольникa C = "))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
elif shape == 2:
    a = int(input("Введите сторону прямоугольника A = "))
    b = int(input("Введите сторону прямоугольника B = "))
    s = a * b
elif shape == 3:
    radius = int(input("Введите радиус круга = "))
    s = math.pi + radius ** 2
else:
    print("Неверный ввод, такой фигуры нет")

print("Общая площадь фигуры:", (round(s, 2)))
