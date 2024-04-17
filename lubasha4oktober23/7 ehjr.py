#Задача 8
# massiv = [8,5,3,2,1,1,0]
# massiv2 = []
# for i in range(len(massiv)-1):
#     print(massiv[i] - massiv[i + 1])
# Задача 9
# massiv = [1,2,3,4,5,7,8]
# massiv2 = []
# for i in range(len(massiv)-1):
#     s = (massiv[i] - massiv[i + 1])
#     if s == -1:
#         print("нет пропущенного числа")
#     elif s != -1:
#         print("пропущено число " + str(massiv[i] + 1))

#Задача 10
massiv = [1,4,8,6,3,9,15,22]
print("укажите чему равна ваша сумма")
sum = int(input())
for i in range(len(massiv)-1):
    s = massiv[i] + massiv[i + 1]
    if s == sum:
        print(massiv[i],massiv[i + 1])
    elif s != sum:
        print("не подходят эти числа")










