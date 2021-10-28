class Worker:

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)
    def get_full_name(self):
        return self.name + self.surname
    def get_full_profit(self):
        self.__income = {'profit': self.profit, 'bonus': self.bonus}
        return self.__income

футболист = Position('Иван' , 'Иванов', 'футболист', 1000000, 300000)
print(футболист.get_full_name(), футболист.get_full_profit())