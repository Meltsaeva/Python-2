# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

from random import randint
print(my_list:= [randint(1, 10) for _ in range(int(input("Input a number of numbers - ")))])
count, result = 0, 0
for item in set(my_list):
    result += my_list.count(item)//2
print(result)
