class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for work car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

BMW = SportCar(250, 'Чёрный', 'BMW', False)
Волга = TownCar(41, 'Белая', 'Волга', False)
VW_Caddy = WorkCar(100, 'Серый', 'VW Caddy', True)
Ford = PoliceCar(200, 'Бело-синий', 'Ford', True)
print(VW_Caddy.turn_left())
print(f'When {Волга.turn_right()}, then {BMW.stop()}')
print(f'{VW_Caddy.name} is {VW_Caddy.color}')
print(f'Is {BMW.name} a police car? {BMW.is_police}')
print(f'Is {Волга.name}  a police car? {Волга.is_police}')
print(BMW.show_speed())
print(Волга.show_speed())
print(Ford.show_speed())