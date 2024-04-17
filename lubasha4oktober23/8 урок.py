# #словари
# '''
#
# {
# "Ключ1": "Значение1"
# "ключ2": "Значение 2"
# }
#
# '''
# student = {
#     "name":  "Алексей",
#     "age": 16,
#     "grande": 9,
#     "otlichnik": False
# }
#
# #Получение информации об ученике
# print('Ученика зовут:',student['name'])
# print('Возраст учениа:',student['age'])
# #print('У ученика есть собака:',student.get ('has_dog'))
# student['has_dog'] = True
#
# #Проверка на наличие ключа в коде
# if student.get('has_dog') == None:
#     print('Мы не знаем есть ли у ученика собака')
# elif student.get('has_dog'):
#     print('У ученика точно есть собака')
# else:
#     print('Скорее всего, у ученика нет собаки')
#
# #Способы удаления записи из словаря
# '''Способ 1'''
# del student ['otlichnik']
# print(student)
# '''Способ 2'''
# student.pop('grande')
# print(student)
#
# #Способы получения всех ключей словаря
# #слева ключ, справа занчение
# print(student.keys())
#
# #Получение всех значений из списка
# print(student.values())
#
# #Получение всех записей словаря
# print(student.items())
#
# #Очистка словаря
# student['name'] = ''
# print(student)
#
# #полная очистка всех данных словаря
# '''первый способ'''
# student.clear()
# print(student)
#
# '''второй способ'''
# student = {}
# print(student)
#
# #Копирование словаря
# student2 = student.copy()
# student2['name'] = 'Александр'
# print(student2)
#
# #Лайфхак
# string  = 'Александр'
# # ['А','л','е','к','с','а','н','д','р']
# letters = []
# for letter in string:
#     letters.append(letter)
# print(letters)
#
# print(string.split())
#
# print([*string])
#
# #Лайфхак 2
# names = 'Алексей;Александр;Андрей'
# #['Алексей', 'Александр', 'Андрей']
# print(names.split(';'))

#Задача 4
a = 'Енот Енот Попугай Енот'
repeats = {
    'Енот': 1
}
words = a.split(' ')
for i in range(len(words)):
    repeats[words[i]] = a.count(words[i])
print(repeats)

#Задача 1 не рабочий вариант
# а  = 1
# в = 1
# е = 1
# и = 1
# н = 1
# о = 1
# р = 1
# с = 1
# т = 1
# д = 2
# к = 2
# л = 2
# м = 2
# п = 2
# у = 2
# б = 3
# г = 3
# ё = 3
# ь = 3
# я = 3
# й = 4
# ы = 4
# ж = 5
# з = 5
# х = 5
# ц = 5
# ч = 5
# ш = 8
# э = 8
# ю = 8
# ф = 10
# щ = 10
# ъ = 10
#
# j = str(input())
# schet = 0
# for i in range(len(j)):
#     if 'a' in j:
#         schet += 1
#     elif 'в' in j:
#         schet += 1
#     elif 'е' in j:
#         schet += 1
#     elif 'и' in j:
#         schet += 1
#     elif 'н' in j:
#         schet += 1
#         print('н', schet)
#     elif 'о' in j:
#         schet += 1
#         print('о', schet)
#     elif 'р' in j:
#         schet += 1
#     elif 'с' in j:
#         schet += 1
#     elif 'т' in j:
#         schet += 1
#         print('т', schet)
#     elif'д' in j:
#         schet += 2
#     elif 'к 'in j:
#         schet += 2
#         print('к', schet)
#     elif 'л' in j:
#         schet += 2
#     elif 'м' in j:
#         schet += 2
#     elif 'п' in j:
#         schet += 2
#     elif' у' in j:
#         schet += 2
#         print('у', schet)
#     elif 'б' in j:
#         schet += 3
#         print('б', schet)
#     elif 'г' in j:
#         schet += 3
#     elif 'ё' in j:
#         schet += 3
#     elif 'ь' in j:
#         schet += 3
#     elif 'я' in j:
#         schet += 3
#     elif 'й' in j:
#         schet += 4
#     elif' ы' in j:
#         schet += 4
#     elif 'ж 'in j:
#         schet += 5
#     elif 'з' in j:
#         schet += 5
#     elif 'х' in j:
#         schet += 5
#     elif 'ц 'in j:
#         schet += 5
#     elif 'ч' in j:
#         schet += 5
#     elif 'ш' in j:
#         schet += 8
#     elif 'э' in j:
#         schet += 8
#     elif 'ю 'in j:
#         schet += 8
#     elif 'ф' in j:
#         schet += 10
#     elif 'щ' in j:
#         schet += 10
#     elif 'ъ' in j:
#         schet += 10
# print(schet)

нро