# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

first = int(input("Input the first number - "))
second = int(input("Input the second number -  "))

def sum_1(first, second):
    if first == 0:
        return second
    else:
        return sum_1(first - 1, second + 1)
    
print(sum_1(first, second))
