# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint

watermelon = int(input("Input a number of watermelons - "))
count, weight, min_water, max_water = 0, 0, 16, 0
while count <= watermelon:
    weight = randint(1, 15)
    print(weight, end=" ")
    count += 1
    if min_water > weight:
        min_water = weight
    elif max_water < weight:
        max_water = weight
print(f'min - {min_water}, max - {max_water}')

