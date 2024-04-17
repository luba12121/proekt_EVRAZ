''''# #Функция - именованный блок кода
# #как записывается:
# #def название_функции(аргумент 1, аргмерн 2):
# #действия которые выполняет функция
#
# #пример функции 1
# def say_hello():
#     print('hello world')
#
# # вызов функции
# say_hello()
# # пример 2  с аргуменом 1
# def print_name(name):
#     print('Тебя зовут',name)
#
# print_name('Артем')
# # второй пример
# user_name = input('напиши как тебя зовут')
# print_name(user_name)
# #Третий пример с операторм return
# def sum_numbers(a, b):
#     return a + b
#
# sum_numbers(a: 2,b: 2)
#
# #4 пример
# def sum_numbers(a,b):
#     return int(a) + int(b)
#
# sum_of_numbers = sum_numbers(a: 2, b: 2)
# print(sum_of_numbers)
#
# # функция без return - процедура
# #функция с return - просто функция


#Пример 4 значение: "по умолчанию"
def multiply(a=2,b=50):
    print(a * b)

multiply()'''

# #задача 1
# def radius(p, r):
#     return p*r**2
#
#
# square = radius(3.14, 5)
# print(square)
#
# #задача 2
# def chislo(a):
#     if a % 3 == 0:
#         return True
#     elif a % 3 != 0:
#         return False
#
# s = chislo(6)
# print(s)
# #Задача 3
# #spisok = [1,2,3]
# def spisok(a,b,c):
#     return max([a, b, c])
#
# d = spisok(1, 200, 3)
# print(d)

#задача 4
def spisokk (a,b,c):
    return a % 2 == 0 and b % 2 == 0 and c %2 == 0



f = spisokk(4,2,6)
print(f)

нОВЫЙ ПРОЕКТИК






