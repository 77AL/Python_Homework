seconds = int(input("Введите время в секундах: "))

h = seconds // 3600
m = (seconds - h * 3600) // 60
s = seconds - (h * 3600 + m * 60)

print(f'{h}:{m}:{s}')