# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.

from random import randint

my_list = []
size = int(input("Input a number of numbers - "))
shift = int(input("Input k - "))


for i in range(size):
    my_list.append(randint(0, 9))

print(*my_list)
print(*my_list[-shift:], *my_list[:len(my_list) - shift])


import random

print(my_list := [random.randint(0, 5) for _ in range(int(input('Введите размер списка: ')))])

shift = int(input('Введите сдвиг: '))

for i in range(100):
    print(my_list[i % len(my_list)], end=' ')

print('\n' + str(my_list[-shift:] + my_list[:-shift]))

for _ in range(shift):
    my_list.insert(0, my_list.pop())
print(my_list)