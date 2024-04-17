cars = '*777 mercedes black*888 bmw blue* '
while True:
    print("выберите одно из перечисленных действий:")
    print("1 Добавить машину")
    print("2 Посмотреть все машины")
    print("3 Редактировать  машину")
    print("4 Удалить машину")
    print("5 Выход")
    answer = int(input("Введите номер команды"))
    if answer  == 1:
        while True:
            print("Приступаем к добавлению машины")
            number = input("Введите номер машины")
            model = input("Введите марку машины")
            color = input("Введите цвет машины")
            car = number + ' ' + model + ' ' + color + '* '
            cars += car
            answer_car = input("Хотите добавить еще машину?")
            if answer_car.lower() == 'да':
                continue
            else:
                break
    if answer == 2:
        print("Просмотр всех машин")
        print(cars)
    elif answer == 3 :
        print("Редактирование машин")
        print("Введите номер машины у которой нужно изменить параметры")
        parametrs = input()
        index_number = cars.find(parametrs)
        index_star = cars.find('* ', index_number)
        new = (cars[index_number:index_star])
        print(new)
        print("Введите новые парамтры")
        car_new = input()
        car_new1 = input()
        car_new2 = input()
        car_new3 = car_new + car_new1 + car_new2
        cars = cars.replace(new, car_new3)

    elif answer  == 4:
        print("Удаление машины")
        print("Введите номер машины которую хотите удалить")
        delete = (input())
        index_number_car = cars.find(delete)
        index_star_car = cars.find('*', index_number_car)
        index_star_car1 = (cars[index_number_car: index_star_car])
        cars = cars.replace(index_star_car1,'')
        print(cars)
        print("машина удалена")
    elif answer  == 5:
        print(" Выход из программы")
        exit()
    else:
        print("Введеная цифра не найдена")




