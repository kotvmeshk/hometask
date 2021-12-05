def int_funk (str):
 i = str[0].upper() + str[1:].lower()
  # return (str.title())
 return (i)

a = input('Введите первое слово:')
b = a.split(" ")
for el in b:
 el = int_funk(el)

 print(f'{el}', end = ' ')