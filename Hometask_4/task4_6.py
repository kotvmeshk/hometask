from itertools import count, cycle

a = int(input('Введите  число:'))
d = int(input('Введите  число больше чем первое:'))

for i in count (a):
    if i > d:
        print("следующее задание:")
        break

    else:
        print(i)
k = 0
for i in cycle ([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]):
    if k > d - 1:
        break
    else:
        print(i)
        k +=1






