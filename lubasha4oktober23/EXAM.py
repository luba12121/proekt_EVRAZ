c
ars = {    'Toyota Camry': {
        'country': 'Япония',        'fuel': 'Гибрид',
        'body_type': 'Седан',        'drive': 'Передний',
        'transmission': 'Автомат'    },
    'Volkswagen Golf.': {        'country': 'Германия',
        'fuel': 'Дизель',        'body_type': 'Хэтчбек',
        'drive': 'Задний',        'transmission': 'Механика'
    },    'Tesla Model X': {
        'country': 'США',        'fuel': 'Электричество',
        'body_type': 'Внедорожник',        'drive': 'Полный',
        'transmission': 'Автомат'    },
    'Ferrari 488 GTB': {
        'country': 'Италия',        'fuel': 'Бензин',
        'body_type': 'Купе',        'drive': 'Задний',
        'transmission': 'Автомат'    },
    'Mazda 3': {        'country': 'Япония',
        'fuel': 'Бензин',        'body_type': 'Седан',
        'drive': 'Передний',        'transmission': 'Автомат'
    },    'Chery Amulet': {
        'country': 'Китай',        'fuel': 'Бензин',
        'body_type': 'Седан',        'drive': 'Передний',
        'transmission': 'Механика'    },
    'BMW 3-Series': {        'country': 'Германия',
        'fuel': 'Дизель',        'body_type': 'Седан',
        'drive': 'Задний',        'transmission': 'Механика'
    },    'Cadillac Escalade': {
        'country': 'США',        'fuel': 'Бензин',
        'body_type': 'Внедорожник',        'drive': 'Полный',
        'transmission': 'Автомат'    },
    'Lamborghini Huracan': {        'country': 'Италия',
        'fuel': 'Бензин',        'body_type': 'Купе',
        'drive': 'Полный',        'transmission': 'Автомат'
    },    'Omoda 55': {
        'country': 'Китай',        'fuel': 'Бензин',
        'body_type': 'Седан',        'drive': 'Передний',
        'transmission': 'Вариатор'    },
}

print("Акинатор. Загадайте машину из выбранных!")for i in cars.keys():
    print(i)countries = ['Италия','Китай','Япония','Германия','Сша']
for country in countries:    s1 = input('Выбранная машина из ' + country)
    a = input()    if country == 'Италия' and a == 'да':
        print("У этой машины Задний привод?")        b = input()
        if b == 'да':            print("Эта машина Ferrari 488 GTB ")
            break        elif b == 'нет':
            print("Эта машина Lamborghini Huracan")            break
    elif country == 'Китай' and  a == 'да':        print("У это машины трансмиссия Вариатор?")
        c = input()        if c == 'да':
            print("та машина Omoda 55 ")            break
        elif c == 'нет':            print("Выбранная машина Chery Amulet ")
            break    elif country == 'Япония' and a == 'да':
        print("У этой машины топливо бензин?")        d = input()
        if d == 'да':            print("Машина Toyota Camry")
            break        elif d == 'нет':
            print("Выбранная машина Mazda 3 ")            break
    elif country == 'Германия' and a == 'да':        print("Тип кузова Хэтчбек?")
        e = input()        if e == 'да':
            print("Ваша машина Volkswagen Golf")            break
        elif e == 'нет':            print("машина BMW 3-Series" )
            break    elif country == 'Сша' and a == 'да':
        print("Машина не нуждается в топливе и потребляет электричество?")        f = input()
        if f == 'да':            print("Ваша машина Tesla Model X ")
            break        elif f == 'нет':
            print("Выбранная машина Cadillac Escalade " )            break
    elif country == 'Сша' and a == 'нет':        print("У нас нет таких машин, вы выбрали что то не то! либо вы написали что то безграмотно, Учите русский язык!")

