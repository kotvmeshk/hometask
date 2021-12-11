
def fact (n):
  num = 1
  for i in range (1, n +1):
   num *= i
   yield num
a = int(input('Введите  число:'))
for el in fact(a):
    print(el)








# from math import factorial
# def fact (n):
#  for n in range (n):
#   print (n)
#   yield factorial(n)
#
# for el in fact(4):
#     print(el)
