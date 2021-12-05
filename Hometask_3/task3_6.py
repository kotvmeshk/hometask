def int_funk (str):
 i = str[0].upper() + str[1:].lower()
  # return (str.title())
 return (i)

a = str(input('Введите первое слово:'))
result = int_funk(a)
print(result)