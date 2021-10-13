profit = int(input("Выручка: "))
expenses = int(input("Издержки: "))

if expenses > profit:
    print("Убыток")
elif profit > expenses:
    print("Прибыль")
    R = (profit - expenses) / profit
    print(f"Рентабельность: {R}")
    staff = int(input("Численность сотрудников фирмы: ")
    Profit_per_worker = (profit - expenses) / staff
    print(f"Прибыль фирмы в расчете на одного сотрудника: {Profit_per_worker}")