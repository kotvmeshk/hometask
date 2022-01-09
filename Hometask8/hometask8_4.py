class Eq:

    def __init__(self, name, model):
        self.__name = name
        self.__model = model
        # self.price = price
        # self.quantity = quantity
        # self.items = {'Модель устройства': self.name, 'Цена за одну единицу': self.price, 'Количество': self.quantity}
    @property
    def full_name (self):
        return f'{self.__name} - {self.__model}'
    # def adding(self):
    #     try:
    #         name = input(f'Введите название: ')
    #         price = int(input(f'Введите цену за одну единицу товара: '))
    #         quantity = int(input(f'Введите количество товара: '))
    #         item = {'Модель устройства': name, 'Цена за одну единицу': price, 'Количество': quantity}
    #         self.items.update(item)
    #         print(self.items)
    #     except ValueError:
    #         print('Недопустимое значение!')


# class Printer(Eq):
#     def __init__(self, name):
#         super().__init__(name)
#         # self.model = model
#
#     def full_name(self):
#         return f'{self.name} '
#
#
# class Scanner(Eq):
#     def __init__(self, name):
#         super().__init__(name)
#         # self.model = model
#
#     def full_name(self):
#         return f'{self.name} '
#
#
# class Xerox(Eq):
#     def __init__(self, name):
#         super().__init__(name)
#         # self.model = model
#
#     def full_name(self):
#         return f'{self.name}  '


class Wh:
    def __init__(self, eq_s=None):
        # self.counterparty = counterparty
        # self.eq = eq
        if not eq_s:
             eq_s ={}
        self.eq_s = eq_s
    def add_eq(self, eq):
        # eq_name = eq.full_name

        result = self.eq_s.get(eq.full_name, None)
        if result:
           self.eq_s[eq.full_name] +=1
        else:
           self.eq_s.update({eq.full_name:1})

    def remove_eq(self,eq ):
        # eq_name = eq.full_name

        result = self.eq.get(eq.full_name, None)
        if result and result > 0:
            self.eq_s[eq.full_name] -= 1

        else:
            print('нет товара на складе')

class Counterparty:
    def __init__(self, category):
        self.category = category
class Department (Counterparty):
    def __init__(self, category):
        super(Department, self).__init__(category)
        self.eq = None
        self.have_eq =False
    def add_eq(self, eq):
        self.eq = eq
        self.have_eq = True


    def remove_eq(self):
        self.eq = None
        self.have_eq = False

class Supplier (Counterparty):
    def __init__(self, category):
        super(Department, self).__init__(category)
        self.eq = None

    def remove_eq(self):
        pass
class Storekeeper (Counterparty):
    def __init__(self, category, wh):
        super(Storekeeper, self).__init__(category)
        self.wh = wh
    def give_eq(self, eq, department):
        if not department.have_eq:
            wh_eq = self.wh.remove_eq(eq)
            if wh_eq:
                department.add_eq(eq)
            else:
                print ('нет единицы товара.')
        else:
            print("оборудование уже установлено")

    def take_eq(self, eq, department):
        if department.have_eq:
            department.remove_eq(eq)
            self.wh.add_eq(eq)

        else:
            print("в отделе оборудование не числится.")





    def take_eq_supl(self, eq, supplier):
        supplier.remuve_eq(eq)
        self.wh.add_eq(eq)

eq1 = Eq('Hp','x300')
eq2 = Eq('Canon','laser jet' )
eq3 = Eq('Xerox', '200')
tot_eq = {eq1.full_name:2,eq2.full_name:4,eq3.full_name:1}
# pri.add_eq()
# sca.add_eq()
# xe.add_eq()
my_wh = Wh(tot_eq)
my_sk = Storekeeper("wh1", my_wh)
# my_sp = Supplier('my_sp')
store = Department('store')
store1 = Department('store1')
store2 = Department('store2')
print ('0 action')
print (my_wh.eq_s)
# print (pri.full_name())
print (store1.eq)
print (store.eq)
print (store2.eq)

print ('1 action')
print (eq1.full_name)
# my_sk.take_eq_supl(eq = sca,my_sp = supplier)
my_sk.give_eq(eq=eq1, department=store1)
print (eq.full_name)

