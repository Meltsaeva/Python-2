# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# my_string = str(input("Input a string - "))
# string_2 = []
# count = {}
# for i in my_string:
#     if i not in count:
#         count[i] = 0
#     else:
#         count[i] += 1
#     if count[i] > 0:
#         string_2.append(f"{i}_{count[i]}")
#     else:
#         string_2.append(i)
# string_2 = ' '.join(string_2)
# print(string_2)

from string import ascii_uppercase
from random import choice

new_line = ''.join([choice(ascii_uppercase + '1234567890') for _ in range(30)])
print(new_line)

dic_count = {}
new_list = []

for ch in new_line:
    dic_count[ch] = dic_count.get(ch, 0) + 1
    if dic_count.get(ch) > 1:
        new_list.append(f'{ch}_{dic_count.get(ch) - 1}')
    else:
        new_list.append(ch)
print(*new_list)