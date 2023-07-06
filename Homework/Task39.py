# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
                # 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

first_number = int(input("Input a number of the first list - "))
second_number = int(input("Input a number of the second list - "))

from random import randint
first_list = [randint(1, 10) for _ in range(first_number)]
second_list = [randint(1, 10) for _ in range(second_number)]
print(first_list, second_list, sep='\n')
third_list = []

for i in range(len(first_list)):
    if second_list.count(first_list[i]) == 0:
        third_list.append(first_list[i])

print(third_list)

