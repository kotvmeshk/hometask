def my_func(sum, stop):
    res = 0
    for i in sum:
        if i == stop :
            break
        res += int (i)
    return res

stopper = "#"
stop = False
s = 0
while not stop:
    inp = input("numbers:").split()
    s += my_func(inp, stopper)
    stop = stopper in inp
    print (f"Сумма:{s}")


# inp = input("numbers:").split()
# my_list = map(int, inp)
# result = my_func(my_list)
#
# inp2 = input("numbers:").split()
# my_list2 = map(int, inp)
# my_list.append [my_list2]
# result = my_func(my_list)