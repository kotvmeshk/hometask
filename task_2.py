a = int(input("введите время в секундах"))

b = a//3600

c = a%3600//60

d = a%3600%60

result_str = f'{b:02}:{c:02}:{d:02}'

print(result_str)


