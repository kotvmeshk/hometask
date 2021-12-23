with open("task5.txt", "w") as file:
    el = input('введите числа через пробелы:')
    el1 = el.split()
    res_el = [int(item)for item in el1]
    total=0
    for num in res_el:
        total +=num
    file.write(el)
    print (res_el)
    print (total)