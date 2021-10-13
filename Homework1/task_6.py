first_day = int(input("Пробег в первый день: "))
must_run = int(input("Должен пробегать: "))
days = 1

while first_day < must_run:
    first_day *= 1.1
    days += 1
print(f"Сколько дней до цели: {days}")