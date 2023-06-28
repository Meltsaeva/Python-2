# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)

# from random import randint

# my_list = [randint(0, 9) for _ in range(10)]
# count = 0
# print(my_list)
# for i in range(1, len(my_list)):
#     if my_list[i] > my_list[i - 1]:
#         count += 1
# print(count)

# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1
# from random import randint

# my_list = [randint(0, 9) for _ in range(10)]
# count = 0
# number = int(input("input a number - "))
# print(my_list)
# for i in range(len(my_list)):
#     if number == my_list[i]:
#         count += 1
# print(count)

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

