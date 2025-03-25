n = int(input("Введите число от 1 до 99: "))
num = n
if 11 <= num <= 14:
    print("У Вас", n, "копеек")
elif 1 <= n <= 99:
    num = num % 10
    if num == 1:
        print( "У Вас", n, "копейка.")
    elif 2 <= num <= 4:
        print("У Вас", n, "копейки.")
    else:
        print("У Вас", n, "копеек.")
else:
    print("Значение должно быть от 1 до 99: ")