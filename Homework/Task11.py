# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

fibonacci = int(input("Input a number - "))
fib1, fib2 = 0, 1
count = 1
while count < fibonacci - 2:
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
print(count if fib2==fibonacci else -1)

