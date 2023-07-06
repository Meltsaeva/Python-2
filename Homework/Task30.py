# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_el = int(input("Input the first element - "))
difference = int(input("Input the difference - "))
num_el = int(input("Input a number of elements - "))

# my_list, i = [], 1
# while i <= num_el:
#     my_list.append(first_el + (i - 1) * difference)
#     i += 1
# print(my_list)

print([(first_el + (i - 1) * difference) for i in range(1, num_el + 1)])