my_dict = {'one':'один', 'two':'два', 'three':'три', 'four':'четыре'}
with open ("task4.txt", "r",encoding='utf-8') as file:
    list = file.readlines()
    # list1 = [ el.strip().split('/n') for el in list]
    new_list = []
    for i in list:
        i = i.split()
        new_list.append(my_dict[i[0]]+i[1]+i[2])
    print (new_list)
with open("task4_2.txt", "w") as file_1:
    # print(new_list, sep= '/n')
    # file_1.writelines(new_list)
    for line in new_list:
        file_1.write(line + '\n')
