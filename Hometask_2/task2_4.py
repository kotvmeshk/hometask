str = input("введите любые слова через пробел: ")
str1 = str.split()
# print(str.len)

i=1
for elk in str1:
    if len(elk) < 10:
        print(i,elk)
    else:
        print(i,elk[:11])
    i+=1

