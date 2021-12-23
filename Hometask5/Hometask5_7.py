import json

with open ("task7.txt", "r") as file:
    items = []
    profit = []
    av_profit = []
    num_h = []
    pr = 0
    for line in file:
     firm, name ,erning,damage = line.split()
     total = int(erning) - int (damage)
     profit.append(total)
     items.append(firm)
     # print(total)
     g = 0
     if total >0:
         pr = total

         av_profit.append(pr)


     else:
         pr = 0

     prof_dict = {}
     for i in range (0, len(items)):
         prof_dict[items[i]]=profit[i]
    b = sum(av_profit)/len(av_profit)

    bdict = dict(avarage_profit = b)
    result = (prof_dict,bdict)
     # b = list1.index('firm_1 OOO 150000 100000')
    print(result)
with open ('test7.json', 'a+', encoding='utf-8' ) as json_file:
    json.dump(result,json_file)
    # # print(dict_avp)
    # print(prof_dict)


#
# import json
# def get_stat():
#     try:
#       with open ('task7.txt','r+',encoding= 'utf-8') as file:
#             stat = []
#             profit = {}
#             av_prof = {}
#             av = 0
#             pr = 0
#             i=0
#             for line in file:
#                 name, firm,erning,damage = line.split()
#                 total = int(erning) - int (damage)
#                 if total >=0:
#                     pr = pr+total
#                 else:
#                     i-=1
#                 profit[name] = total
#             stat.append(profit)
#             if i !=0:
#                 (av) = pr/i
#                 av_prof['av_prof'] = round (av)
#                 stat.append(av_prof)
#             else:
#                 print('все компании работают в убыток')
#             print(stat)
#       with open('file_task7.json', 'a+', encoding ='utf-8' )  as json_file:
#             json.dump(stat,json_file)
#      # except FileNotFoundError:
#      #    return 'файл не найден'