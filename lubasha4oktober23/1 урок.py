# Переменная - именнованный контейнер , содержащий какие то данные
name = 'luba'
age = 13
print (name)
# функция print выводит информацию в консоль
#Типы данных в пайтоне
# целое число integer
integer = 24
#float дробное число
FL = 24.4
#string() строка
stroka1 = 'яблоко'
stroka2 = "апельсин"
num = '123'
#boolean правда или ложь
es_morning = False #Ложь
es_evning = True # Правда
#Преобразование типов
num = '22'
print (type(num))
int () # преобразоаниев целое число
num = int(num)
print (type(num))

#float() преобразование в дрбное число
num = float(num)
print(num)
#bool -преобразование типа данных в равду или ложь
num = bool(num)
#str - преобразование данных в строку
num = str(num)
print(type(num))
#Операции над данными
num1 = 12
num2 = 13
#сложение чисел
print(num1 + num2)
print(str(num1) + str(num2))

#вычитание чисел
print(num1 - num2)
#Вычитать строки нельзя!!!
#умножение чисел
print(num1*num2)
print(str(num1) * 4)
#деление чиел
print(100/5)
print(10//3)
print(10%3)
#Возведение числа в степень
print(10**3) #ответ 1000
#input()  функци ввода данных на консоле
user_name1 = input('Привет, напиши свое имя ')
user_age2 = input(' напиши свой возраст ')
print ('Тебя зовут:' + user_name1)
print ('Тебе :' + user_age2)



