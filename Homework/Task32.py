# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint

min_num = int(input("Input the minimun value - "))
max_num = int(input("Input the maximum value - "))
number = int(input("Input a number of numbers - "))

print(my_list := [randint(-20, 20) for _ in range(number)])

# for i in range(number):
#     if min_num <= my_list[i] <= max_num:
#         print(i)

index = [i for i, numb in enumerate(my_list) if min_num <= numb <= max_num]
print(index)