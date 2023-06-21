# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint
coins = int(input("Input a number of coins - "))
count, heads_tails, count_coins = 1, 0, 0

while count <= coins:
    heads_tails = randint(0, 1)
    print(heads_tails, end=" ")
    count += 1
    if heads_tails > 0:
        count_coins += 1
if count_coins > coins / 2:
    print('\n', coins - count_coins)
else:
    print('\n', count_coins)


