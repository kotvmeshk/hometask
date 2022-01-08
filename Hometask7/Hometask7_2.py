from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Использованная ткань : {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Не все данные'


class Coat(Clothes):
    def consumption(self):
        return f'Необходимо для пальто: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Не все данны 2'


class Costume(Clothes):
    def consumption(self):
        return f'На костюм требуется: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass


coat = Coat(850)
costume = Costume(60)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())