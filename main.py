import pandas as pd


class Car:
    def __init__(self, brand, model, release, price):
        self.brand = brand
        self.model = model
        self.release = release
        self.price = price


car1 = Car('BMW', 'M3 F80', 2014, 3550.00)
car2 = Car('Ferrari', '488 GTB', 2015, 20700.00)
car3 = Car('Porsche', 'Cayman S', 2007, 2130.00)
car4 = Car('Volkswagen', 'Tiguan', 2019, 2277.00)
car5 = Car('Mercedes-Benz', 'S-класс', 2005, 990.00)

carArray = [car1, car2, car3, car4, car5]


while True:
    print('Выберите действие:')
    print('1 - Вывод всех объектов')
    print('2 - Выход из программы.')
    print('3 - Добавление нового объекта')
    print('4 - Удаление объекта')

    print('5 - Сортировка по свойству')
    print('6 - Фильтрация')
    print('7 - Преобразование')

    v = input()
    if v not in ('1', '2', '3', '4', '5', '6', '7'):
        print('Неверный выбор')
        print('Попробуйте еще раз\n')
        continue

    brands = [i.brand for i in carArray]
    models = [i.model for i in carArray]
    releases = [i.release for i in carArray]
    prices = [(str(i.price) + ' тыс. руб.') for i in carArray]
    df = pd.DataFrame({"Марка автомобиля": brands,
                       "Модель": models, "Год выпуска": releases, "Цена": prices})

    if v == '1':
        if (len(carArray) != 0):
            print(df)

        else:
            print("Автосалон пуст.")
    elif v == '2':
        print("До встречи!")
        break
    elif v == '3':
        if (len(carArray) < 12):
            brand = input("Введите марку авто: ")
            model = input("Введите модель: ")
            release = int(input("Введите год выпуска: "))
            price = float(input("Введите цену в тыс. руб.: "))
            newCar = Car(brand, model, release, price)
            carArray.append(newCar)
        else:
            print("Автосалон полон.")
    elif v == '4':
        if (len(carArray) == 0):
            print("Автосалон пуст")
            continue
        choice = int(input("Введите номер объекта, который хотите удалить: "))
        if choice >= 0 and choice < len(carArray):
            carArray.pop(choice)
        else:
            print("Автомобиля с таким номером не существует.")
    elif v == '5':
        print('Введите свойство:')
        print('1 - Марка')
        print('2 - Модель')
        print('3 - Год выпуска')
        print('4 - Цена')

        carProperty = int(input())
        if carProperty == 1:
            carArray = sorted(carArray, key=lambda x: x.brand)
        elif carProperty == 2:
            carArray = sorted(carArray, key=lambda x: x.model)
        elif carProperty == 3:
            carArray = sorted(carArray, key=lambda x: x.release)
        elif carProperty == 4:
            carArray = sorted(carArray, key=lambda x: x.price)
        else:
            print('Нет свойства с таким номером.')
    elif v == '6':
        year = int(input('Введите год выпуска: '))
        newDf = df.loc[df["Год выпуска"] >= year]
        print(newDf)

    elif v == '7':
        percent = int(input('Введите процент скидки: '))
        for i in carArray:
            i.price = i.price - i.price * percent/100
    print()
