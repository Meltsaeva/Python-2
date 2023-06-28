# Требуется найти в массиве list_1 самый близкий по величине элемент 
# к заданному числу k и вывести его.

# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5
from random import randint

k = int(input("input a number - "))
list_1 = [randint(0, 9) for _ in range(10)]
print(list_1)
count, min_dif, j = 0, float ( "inf" ), 0
for i in range(len(list_1)):
    difference = abs(k - list_1[i])
    if min_dif > difference:
        min_dif = difference
        j = list_1[i]
print(j)