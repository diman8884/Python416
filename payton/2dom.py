n = input("Введите пятизначное число: ")
a = n
a = str(a)
sum = int(a[0]) * int(a[1]) * int(a[2]) * int(a[3]) * int(a[4])
f = int(a[0]) + int(a[1]) + int(a[2]) + int(a[3]) + int(a[4])
suma = f / 5
print("Произведение числа", n, ":", sum)
print("Среднее арифмитическое:", suma)