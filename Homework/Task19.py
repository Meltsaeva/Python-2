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
