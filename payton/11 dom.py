s1 = input("Введите первую строку:")
s2 = input("Введите вторую строку:")
s1 = set(s1)
s2 = set(s2)
a = s1 - s2
print("Отсутствующие буквы во второй строке:")
for i in a:
    print(i, end=" ")