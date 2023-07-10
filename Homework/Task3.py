# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

first_class = int(input("Input a number of students of the first class- "))
second_class = int(input("Input a number of students of the second class- "))
third_class = int(input("Input a number of students of the third class- "))

desks = int((first_class + 1) / 2)+ int((second_class + 1) / 2)+ int((third_class + 1) / 2)
print(desks)