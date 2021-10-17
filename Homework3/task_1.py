def division(a, b):
    if b == 0:
        return "Нельзя делить на 0!"
    else:
        return a/b

a = int(input('a: '))
b = int(input('b: '))
print(division(a,b))