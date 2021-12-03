a = "12345678"
str_reverse = ''
b = list(a)
for el in range (len(a) // 2):
    tmp = b[el]
    b[el] = b[len (a) - el -1]
    b[len(a)-el-1] = tmp
str_reverse = ''.join (b)
print (str_reverse)
