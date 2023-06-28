# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}]
my_list = []
for items in dictionary:
    for value in items.values():
        my_list.append(items[value])
print(my_list)






# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

# count, min_dif, j = 0, float ( "inf" ), 0
# for i in range(len(list_1)):
#     difference = abs(k - list_1[i])
#     if min_dif > difference:
#         min_dif = difference
#         j = list_1[i]


# ребуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -

# from random import randint
# number = int(input("Input a number - "))
# my_array = [randint(0, 9) for _ in range(number)]
# print(my_array)
# unknown = int(input("Input x - "))
# print(my_array.count(unknown))

# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# string_1 = str(input("Input a string - "))
# simbols = string_1.split()
# print(simbols)
# string_2 = []
# count = {}
# for i in simbols:
#     if i not in count:
#         count[i] = 0
#     else:
#         count[i] += 1
#     if count[i] > 0:
#         string_2.append(f"{i}_{count[i]}")
#     else:
#         string_2.append(i)
# string_2 = ' '.join(string_2)
# print(string_2)

# my_string = str(input("Input a string - "))
# string_2 = []
# count = {}
# for i in my_string:
#     if i not in count:
#         count[i] = 0
#     else:
#         count[i] += 1
#     if count[i] > 0:
#         string_2.append(f"{i}_{count[i]}")
#     else:
#         string_2.append(i)
# string_2 = ' '.join(string_2)
# print(string_2)

