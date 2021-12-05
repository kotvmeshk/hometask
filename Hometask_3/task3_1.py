def funk_1 (mn_1, mn_2):

    if mn_2 == 0:
     return print('на 0 делить нельзя!')
    else:
     res = mn_1 / mn_2
     return print(res)



a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
result = funk_1(a,b)


