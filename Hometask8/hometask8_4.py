class Equip:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель устройства': self.name, 'Цена за одну единицу': self.price, 'Количество': self.quantity}

    def adding(self):
        try:
            name = input(f'Введите название: ')
            price = int(input(f'Введите цену за одну единицу товара: '))
            quantity = int(input(f'Введите количество товара: '))
            item = {'Модель устройства': name, 'Цена за одну единицу': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(Equip):
    pass


class Scanner(Equip):
    pass


class Xerox(Equip):
    pass


pri = Printer('Hp', 2, 300)
sca = Scanner('Canon', 54000, 10)
xe = Xerox('Xerox', 7000, 15)
pri.adding()
sca.adding()
xe.adding()