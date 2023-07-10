# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)

from random import randint

my_list = [randint(0, 9) for _ in range(10)]
count = 0
print(my_list)
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        count += 1
print(count)