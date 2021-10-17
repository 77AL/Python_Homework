input = input("Введите значение списка: ")
list = input.split ()
len_list = len(list)
i = 0
if len_list > 1:
    while i < len_list - 1:
        list[i], list[i+1] = list[i+1], list[i]
        i += 2
print(list)