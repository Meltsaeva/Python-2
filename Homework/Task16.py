# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1
from random import randint

my_list = [randint(0, 9) for _ in range(10)]
count = 0
number = int(input("input a number from 0 to 9 - "))
print(my_list)
for i in range(len(my_list)):
    if number == my_list[i]:
        count += 1
print(count)

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