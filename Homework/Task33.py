# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random

def creat_journal(objs: int) -> list[int]:
    return [random.randint(1, 5) for _ in range(objs)]


def hack_journal(journal: list[int]) -> list[int]:
    max_mark = max(journal)
    min_mark = min(journal)
    return[mark if mark != max_mark else min_mark for mark in journal]

my_j = creat_journal(int(input("Input a number of grades - ")))
print(my_j)
print(hack_journal(my_j))
    

number_grades = int(input("Input a number of grades - "))