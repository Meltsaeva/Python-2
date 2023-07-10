# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

first_number = int(input("Input a number of elements of the first set - "))
second_number = int(input("Input a number of elements of the second set - "))

first_set = {randint(0, 9) for _ in range(first_number)}
second_set = {randint(0, 9) for _ in range(second_number)} 
print(first_set, second_set, sep = '\n') 

new_set = first_set.intersection(second_set)
print(sorted(new_set))