from sys import argv

worked_hour, rate_per_hour, bonus = argv

print("Выработка в часах: ", worked_hour)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", bonus)

formula = (int(worked_hour) * int(rate)) + int(bonus)
print(f"Ваша зарплата равна {formula}")