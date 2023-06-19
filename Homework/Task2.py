# Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Input a number - "))
first_number = number //100
second_number = number //10 % 10
third_number = number % 10
sum_numbers = first_number + second_number + third_number
print(f"{sum_numbers} ({first_number} + {second_number} + {third_number} )")