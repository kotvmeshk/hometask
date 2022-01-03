class Cars:
    def __init__(self, speed, color, name, is_police = True):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'
    def stop(self):
        return f'{self.name} остановилась.'
    def turn(self, direction):
        self.direction = direction
        return f'{self.name} повернула {self.direction}.'
    def show_speed(self):
        return f' скорость {self.name} - {self.speed}. '


class TownCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'ОСТОРОЖНО! скорость {self.name} - превышена '
        else:
            return f' скорость {self.name} - {self.speed} в пределах нормы '

class SportCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'ОСТОРОЖНО! скорость {self.name} - превышена '
        else:
            return f' скорость {self.name} - {self.speed} в пределах нормы '

class PoliceCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


a = SportCar(300,'черный', 'Porshe', False)
print(a.go(), a.show_speed(), a.turn('налево'), a.stop())

b = WorkCar(45,'синий', 'трактор', False)
print(b.go(), b.show_speed(), b.turn('направо'), b.stop())

c = PoliceCar(120,'сине - белая', 'полицейская машина', True)
print(c.go(), c.show_speed(), c.turn('направо'),c.turn('направо'), c.turn('налево'), c.stop())

d = TownCar(55,'белая', 'Volvo', False)
print(d.go(), d.show_speed(), d.turn('налево'), d.stop())
