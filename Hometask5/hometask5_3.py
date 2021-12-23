with open ("task3.txt", "r") as file:
  all = []
  line = []
  list = file.readlines()

  for i in list:
    i = i.split()
    all.append(i[1])
    res_all=[int(item)for item in all]
    aver = sum(res_all)/len(all)
    if int(i[1]) < 20000:
      line.append (i[0])
  # print(aver)
  print (f'Оклад меньше 20000 у:{line}, средний оклад по всей компании: {aver}.')



   # res = f"hdgsg'{content}'"
  # print(list)
