input = input("Ваше предложение: ")

words = input.split()

for number, word in enumerate(words):
    print (f'{number}, {word[:10]}')