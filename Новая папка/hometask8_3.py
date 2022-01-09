class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.ls = []

    def check_value(self):
        global inp_number
        while True:
            try:
                try:
                    inp_number = int(input('Введите числа: '))
                    inp_ch = input(f'"{inp_number}" добавлен в список. Хотите продолжить? y/n: ').lower()
                    self.ls.append(inp_number)
                    if inp_ch == 'n':
                        print(self.ls)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                inp_ch = input(f"Введенные данные некорректны! Хотите продолжить? y/n: ").lower()
                if inp_ch == 'n':
                    print(self.ls)
                    break
                else:
                    self.check_value()
# fguiuoi

a = TypeCheck()
a.check_value()

