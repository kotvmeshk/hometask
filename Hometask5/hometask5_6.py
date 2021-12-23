num_h = {}
with open ("task6.txt") as file:


     # num_h = [[0 for j in range(3)] for i in range(5)]

    list = file.readlines()

    for line in list:
         list1 = line.split()
         i = 0
         for elem in list1[1:]:
             if elem !='-':
                 num = '0'
                 for c in elem:
          # el = ' '.join(el)

                    if c.isdigit():
                       num += c
                  # num_h.append(c)
             # print(num_h)
             # i += 1

              # elif len(c)>5:
              #     items.append(c)
              #     c == 0
                    else:
                         break
                 i +=int (num)
    # el = el.split()
    # el.append(c)
         num_h.update({list1[0]:i})
    print (num_h)
    # print(el)
