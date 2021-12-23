with open ("task1.txt", "w") as file:
   while True:
     el = input('введите текст:\n')
     file.write (el + '\n')
     if not el:
         break




   # while el:
   #  el = input('введите текст\n')
   # file.whritelines(el)

    # if not el:
    #  break
