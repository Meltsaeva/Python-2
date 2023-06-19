# Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

length = int(input("Input the length of the chocolate bar " ))
width = int(input("Input the width of the chocolate bar "))
slice = int(input("Input the number of chocolate slices "))

if length * width > slice:
    if slice % length == 0 or slice % width == 0:
        print("Yes")
    else:
        print("No")
else:
    print("Incorrect")
