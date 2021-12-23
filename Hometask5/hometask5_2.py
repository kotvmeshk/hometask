with open ("task2.txt", "r") as file:
 result = file.readlines()


 i=0
for num,line in enumerate(result):
      i+=1
      k = len(line.split())
      print (f'Кодичество слов в', i, 'ой строке -' ,k)
print('Количество строк:', i)
    #  f = (len(line.split(' '))
    #         f=f*2
    # print (p)
       # with open("task2.txt", "r") as file:

