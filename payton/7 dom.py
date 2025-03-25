import random

randon_number = [random.randint(0, 100) for i in range(10)]
print("Случайные числа списка:", randon_number)
mas = randon_number.copy()
mas.sort()
min_ = mas[0]
print("Минимальное число:", min_)
ind = randon_number.index(min_)
print("Минимальны индекс:", ind) # минимальный индекс
del randon_number[:ind]
print("Числа перед минимальным числом списка:", randon_number)