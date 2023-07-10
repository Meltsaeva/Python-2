# По данному целому неотрицательному n вычислите значение n!.
#  N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

num = int(input("Input N - "))
count = 1
result = 1

if num > 0:
    while count <= num:
        result *= count 
        count += 1
    print(result)
else:
    print("Incorrect")