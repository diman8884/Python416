n = [0] * int(input("Введите колличество элеменов списка: "))
for i in range(len(n)):
    n[i] = int(input("-> "))
print("Введеные цисла", n)
sum = 0
for i in range(len(n)):
    if n[i] < 0:
        sum += n[i]
print("Сумма отрицательных чисел:",sum)

