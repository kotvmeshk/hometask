my_list = [7,5,3,3,2]
a = int(input("Введите элемент:"))
idx = False
for l,  num in enumerate (my_list):
     if a > num :
        my_list.insert(l, a)
        idx = True
        break

else:
    my_list.apend (a)

print (my_list)
