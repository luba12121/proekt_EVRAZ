#print(a>=b)
# Первое число (а) больше или равно второму числу (b)
#print(a<=b)
# Первое число (а) меньше или равно второму числу (b)
#print(a!=b)
# Первое число (а) неравно второму числу (b)
#print(a!=b)
# Первое число (а) равно второму числу (b)
#Условия
#if условие выполняется (True)
#print("условие истиное то есть равнется True")
'''if a > b:
    print("число а больше b")
#else(Иначе)
if a >= b
    print("число а меньше или равно числу b")
else:
    print ("число а больше числа b")

if a < b:
    print("число а меньше числа b")
else:
    print("число а больше числа b")
# elif иначе если
if a < b:
    print("число а меньше числа b")
elif a == b:
    print("числа равны")
else:
    print("число а больше числа b")'''
#and и
#or или

'''a = 14
b = 10
c = 24
if a > b and a < c:
    print("а среднее число")

if a % 2 == 0 and  a >= 0:
    print ("a четное положительное число")
else:
    print("ошибка")

if b % 2 == 0 or b>=0:
    print("чсло b четное или положительное")
else: 
    print("ошибка")'''

#print(14 == "14")

# задачи
#1
'''a = int(input())
if a > 0:
    print(a+1)
else:
    print(a)
#2
a = int(input())
if a > 0:
    print(a+1)
else:
    print(a-2)
#3
if a > 0:
    print(a+1)
elif a < 0:
    print(a-2)
else:
    print(a==10)
    print(a)
#4
a = int(input())
b = int(input())
c = int(input())
if a >= 0 and b >= 0 and c >= 0:
    print("3 положительных числа")
elif a < 0 and b >= 0 and c >= 0:
     print ("2 числа положительных")
elif a < 0 and b < 0 and c >0:
    print("1 число положительное")
elif a < 0 and b < 0 and c < 0:
    print("нет положительных чисел")
elif a >= 0 and b < 0 and c >= 0:
    print("2 положительных числа")
elif a >= 0 and b < 0 and c < 0:
    print("1 положительное число")
elif a >= 0 and b >= 0 and c < 0
    print("2 положительных числа")
#5
a = int(input())
b = int(input())
c = int(input())
if a >= 0 and b >= 0 and c >= 0:
    print("3 положительных числа")
elif a < 0 and b >= 0 and c >= 0:
     print ("2 числа положительных 1 отрицательное")
elif a < 0 and b < 0 and c >0:
    print("1 число положительное 2 отрицательных")
elif a < 0 and b < 0 and c < 0:
    print("нет положительных чисел все отрицательные")
elif a >= 0 and b < 0 and c >= 0:
    print("2 положительных числа 1 отрицательное")
elif a >= 0 and b < 0 and c < 0:
    print("1 положительное число 2 отрицательных")
elif a >= 0 and b >= 0 and c < 0
    print("2 положительных числа 1 отрицательное")
#6
a = int(input())
b = int(input())
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("они равны")
#7
a = int(input())
b = int(input())
if a < b:
    print("1")
elif b < a:
    print("2")
#8
a = int(input())
b = int(input())
if a > b:
    print (a)
    print (b)
elif b > a:
    print(b)
    print(a)
#9
A = int(input())
B = int(input())
if A > B:
    print(B > A)
    print (A and B)
elif B > A:
    print(A > B)
    print (A and B)
#10
a = int(input())
b = int(input())
if a != b:
    a = a+b
    b = a + b
    print (a and b)
elif a == b:
    a = 0
    b = 0
    print (a and b)'''
#11
a = int(input())
b = int(input())
if a != b:
    if a > b:
        b = a
        print (a and b)
    elif b > a:
        a = b
    print(a and b)
elif a == b:
    a = 0
    b = 0
    print(a,b)
#12
a = int(input())
b = int(input())

