def my_func(arg1,arg2,arg3):
    mylist = [arg1,arg2,arg3]
    mylist.sort(reverse=True)
    res = mylist[0] + mylist[1]
     # if arg1 > arg2:
     #    max1 = arg1
     # else:
     #    max1 = arg2
     # if arg3 > arg2:
     #    max2 = arg3
     # else:
     #    max2 = arg2
     # res = max1 + max2
     #
    return (res)

a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))
result = my_func (a,b,c)

print (result)

