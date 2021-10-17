def int_func(football):
    word = football[0].upper + football[1:].lower()
    return word

input = input("Введите слово: ")
for word in input.split():
    print(f'{int_func(word)}')