# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

my_string = str(input("Input a string - "))
string_2 = []
count = {}
for i in my_string:
    if i not in count:
        count[i] = 0
    else:
        count[i] += 1
    if count[i] > 0:
        string_2.append(f"{i}_{count[i]}")
    else:
        string_2.append(i)
string_2 = ' '.join(string_2)
print(string_2)

