# Дано натуральное число N и
# последовательность из n элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def numbers(n):
    if n == 0:
        return
    number = int(input("Input N - "))
    numbers(n - 1)
    print(number, end = " ")
n = int(input("Input a number of numbers - "))    
numbers(n)