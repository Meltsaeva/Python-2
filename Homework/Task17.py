# Дан список чисел. Определите,
# сколько в нем встречается различных чисел.

from random import randint

my_list = rez = []
size = int(input("Input a number of numbers - "))


for i in range(size):
    my_list.append(randint(0, 9))

print(*my_list)

for i in range(len(my_list)):
    if res.count(my_list[i])<1:
        res.append(my_list[i]) 
