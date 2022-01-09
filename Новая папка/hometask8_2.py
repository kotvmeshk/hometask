class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

# gkhh
def div():
    try:
        inp_divisible = int(input('Введите делимое: '))
        inp_divider = int(input('Введите число, на которое нужно разделить: '))
        if inp_divider == 0:
            raise OwnError("Деление на ноль невозможно!")
        else:
            result = inp_divisible / inp_divider
            return result
    except ValueError:
        return "Введенные данные некорректны!"
    except OwnError as error:
        return error


print(div())