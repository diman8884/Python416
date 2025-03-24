# рекурсия

# def elevator(n): # 3
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n -1) # стек 5 4
#     print(n, end=" ")
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
# print(sum_list([1, 3, 5, 7, 9]))
#
# def sum_list(lst):# {1, 3, 5, 7, 9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:]) # 1 + 3 + 5 + 7 +9
# print(sum_list([1, 3, 5, 7, 9])) # 25

# def to_str(n, base): # n = 254, base = 16
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n] # 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base] # 'F' + 'E'
# print(to_str(254, 16))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#     else:
#         count += 1
#     return count
#
# print(count_items(names))

# 20.03

# dom
# def negative_number(n): # [шаг1 -2, шаг2 3, шаг3 8, шаг4 -11, шаг5 -4, шаг6 6] после всех циклов пустой список в итоге
#     if not n: # if len(n) == 0
#         return 0
#     count = 0 # 0 или 1
#     if n[0] < 0:
#         count += 1
#     return count + negative_number(n[1:]) # 1 + 0 + 0 + 1 + 1 + 0
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negative_number(lst))

