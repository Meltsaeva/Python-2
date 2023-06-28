# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}]
my_list = []
for items in dictionary:
    for value in items.values():
        my_list.append(items[value])
print(my_list)












# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# string_1 = str(input("Input a string - "))
# simbols = string_1.split()
# print(simbols)
# string_2 = []
# count = {}
# for i in simbols:
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

