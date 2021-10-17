month_num = input("Введите номер месяца: ")
z, v, l, o = "зима", "весна", "лето", "осень"
list = [z, z, v, v, v, l, l, l, o, o, o, z]
print(list[int(month_num) - 1])

dictionary = {'1': z, '2': z, '3': v, '4': v, '5': v, '6': l, '7': l, '8': l, '9': o, '10': o, '11': o, '12': o}
print(dictionary[month_num])