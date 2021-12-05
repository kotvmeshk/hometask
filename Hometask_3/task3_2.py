def inf_list (arg1,arg2,arg3,arg4,arg5,arg6):
 mydict = {"Имя":arg1,"фамилия":arg2,"год рождения":arg3,"город проживания":arg4,"e-mail":arg5,"телефон":arg6}
 return mydict

a = input('Введите имя:')
b = input('Введите фамилию:')
c = input('Введите год рождения:')
d = input('Введите город проживания:')
e = input('Введите e-mail:')
f = input('Введите телефон:')

result = inf_list(arg1=a,arg2=b,arg3=c,arg4=d,arg5=e,arg6=f)
print (result)