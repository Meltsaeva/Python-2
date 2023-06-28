# Дан список чисел. Определите,
# сколько в нем встречается различных чисел.

from random import randint

my_list = []
size = int(input("Input a number of numbers - "))


for i in range(size):
    my_list.append(randint(0, 9))

print(*my_list)
print(set(my_list))
print(len(set(my_list)))