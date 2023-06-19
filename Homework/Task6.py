# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket = int(input("Input a ticket number - "))

first_number = ticket // 100000 
second_number = (ticket % 100000) // 10000
third_number = (ticket % 10000) // 1000
fourth_number = (ticket % 1000) // 100
fifth_number = (ticket % 100) // 10 
sixth_number = ticket % 10

print(first_number, second_number,third_number,fourth_number,fifth_number,sixth_number)

sum_one = first_number + second_number + third_number
sum_two = fourth_number + fifth_number + sixth_number

if sum_one == sum_two:
    print("Yes")
else:
    print("No") 