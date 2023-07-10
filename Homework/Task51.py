# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)


my_func = lambda x : x % 2 == 0
new_object = ['s', 's', 's', 's', 'w']
def same_by (func, my_object):
    res = list(filter(func, my_object))
    if len(res) == len(my_object):
        return True
    return False

print(same_by(lambda x : len(x) == 1, new_object))

