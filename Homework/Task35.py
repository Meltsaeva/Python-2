# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

import random

print(simple_number:=(random.randint(0, 1000)))

def check(simple_number):
    if simple_number < 2:
        return False
    for i in range(2, int(simple_number ** 0.5) + 1):
        if simple_number % i  == 0:
            return False
    return True

print(check(simple_number))
