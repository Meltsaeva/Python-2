# Петя, Катя и Сережа делают из бумаги журавликов.
#  Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# S= x+4x+x
# x = S/6

crane = int(input("Input a number of cranes - "))
petya_serg = int(crane / 6)
kate = int(petya_serg * 4)
print(f"Peter made {petya_serg}, Kate made {kate}, Sergey made {petya_serg}")