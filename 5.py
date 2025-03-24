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

# for element in collections:
#         print(element)

# for i in "Hello":
#     print(i)
#
# for i in "Hello", "World":
#     print(i)

# range(start = 0, stop, step=1)

# print(range(11))
# for i in range(1, 10, 1):
#     print(i, end =" ")
#
# print()
# j = 1
# while j < 10:
#     print(j, end = " ")
#     j += 1

# for i in range(10, 0, -1):
#     print(i, end =" ")
#
# print()
# j = 10
# while j > 0:
#     print(j, end = " ")
#     j -= 1

# a = int(input("Введите первое число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end =" ")
#
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     if i == 1:
#         print(i)
# else:
#     print("Конец цикла")

# for i in range(3): # for(let i = 0; i < 3; i++) i = 3
#     print("+++")
#     for j in range(2): # for(let j = 0; j < 2; j++) i = 2
#         print("_____")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):#0
#     for j in range(w):# 12
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# string = [letter + 4 for letter in "Python"]
# print(string)
# for letter in "Python":
#     print(letter + 4, end="\t")

# num = [i for i in range(30)]
# print(num)
# print()
# for i in range(30):
#     print(i, end="\t")

#Список(List)
# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(type(nums))

# num1 = list([8, 3, 9, 4, 1])
# print(num1)
# print(type(num1))
#
# num1 = List[]
# list(num1)
# print(type(num1))

# nums = [8, 3, 9, 4, 1 ]
# print(nums[0])
# print(nums[-5])
# print(nums[4])
# print(nums [-1])

# nums = [8, 3, 9, 4, 1 ]
# print(nums)
# nums[1] = 256
# print(nums)
# nums[3] += 100

# nums = [8, 3, 9, 4, 1 ]
# print(nums, id(nums))
# print(nums[0], id(nums[0]))
# print(nums[1], id(nums[1]))
# nums[1] = 256
# print(nums[1], id(nums[1]))
# print(nums, id(nums))
# print("Длина списка: ", len(nums))

# nums = [8, 3, 9, 4, 1 ]
# nums2 = [11, 12, 13]
# n = nums + nums2
# print(n)
# print(n * 2)

# print(list("Hello"))

# print(list("Hello"))
# print(range(10))
# print(list(range(10)))
# print(list(range(2, 10)))
# print(list(range(10, 2, -2)))

#[выражение  for переменная in последовательность]

# a = [0 for _ in range(5)] # 0 1 2 3 4 5
# print(a) #[0 0 0 0 0]


# a = ["*" for _ in range(5)] # 0 1 2 3 4 5
# print(a) #[0 0 0 0 0]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a) #[1, 4,9, 16]

# a = [0] * int(input("Введите колличество элеменов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("->") for i in range(int(input("n = ")))]
# print(a)