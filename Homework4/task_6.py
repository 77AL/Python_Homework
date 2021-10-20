from intertools import count, cycle

n = 50

my_list = [el for el in range(10)]
counter = count()
cycler = cycle(my_list)

print([next(counter) for el in range(n)])
print([next(cycler) for el in range(n)])