def my_func (x,y):
    if x < 0 :
        print ("число введено не верно")
        return ("операцию невозможно выполнить")
    elif  y > 0 :
        print("число введено не верно")
        return ("операцию невозможно выполнить")
    else:
        b = x ** y
    return b
a = int(input('Введите действительное положительное число:'))
b = int(input('Введите отрицательное целое число:'))

result = my_func(a,b)
print(result)