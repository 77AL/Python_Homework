file = open('test.txt', 'w')
line = input('Введите текст: \n')
while line:
    file.write(line)
    line = input('Введите текст: \n')
    if not line:
        break