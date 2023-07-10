# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

first_number = int(input("Input the first number- "))
second_number = int(input("Input the second number - "))

def degree(first_number, second_number):
    if second_number == 0:
        return 1
    else:
        return first_number * degree(first_number, second_number - 1)

print(degree(first_number, second_number))