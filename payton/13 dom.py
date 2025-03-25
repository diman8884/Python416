a = {}

n = int(input("Кол-во студентов: "))
s = 0
for i in range(n):
    name = input(str(i + 1) + "-й студент: ")
    point = int(input("Балл: "))
    a[name] = point
    s += point
average = s / n

print("Средний балл: ", round(average), " Студенты с баллом выше среднего: ", sep="")

for i in a:
    if a[i] > average:
        print(i)