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