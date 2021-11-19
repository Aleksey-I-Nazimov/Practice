# ---------------------------------------------------------------------
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав
# описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.
import json

import jsons


class Colors:
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'

    @staticmethod
    def validate(color):
        if Colors.GREEN != color and Colors.YELLOW != color and Colors.RED != color:
            message = "Unknown color set {}".format(color)
            raise Exception(message)


class ColorPosition:
    def __init__(self, color, switch_time_ms, position):
        self.__color = color
        self.__switch_time_ms = switch_time_ms
        self.__position = position

    def get_color(self):
        return self.__color

    def get_switch_time(self):
        return self.__switch_time_ms

    def get_position(self):
        return self.__position

    def __str__(self):
        return json.JSONEncoder().encode(jsons.dump(self))


class ColorSwitcher:
    def __init__(self):
        red = ColorPosition(Colors.RED, 7000, 2)
        yellow = ColorPosition(Colors.YELLOW, 1000, 1)
        green = ColorPosition(Colors.GREEN, 30000, 0)
        self.__color_position_list = [red, yellow, green]
        self.__color_position_map = {Colors.RED: red, Colors.YELLOW: yellow, Colors.GREEN: green}
        self.__index = 0
        self.__limit = len(self.__color_position_list)
        self.__reverse = False

    def next_color(self, **args):
        next_color = args.get("next")
        if next_color is not None:
            return self.__next_position_set(next_color)
        else:
            return self.__next_position_seq()

    def current_color(self):
        return self.__color_position_list[self.__index]

    def __next_position_seq(self):
        if self.__reverse:
            self.__index = self.__index - 1
        else:
            self.__index = self.__index + 1
        if self.__index == self.__limit:
            self.__index = self.__index - 2
            self.__reverse = True
        if self.__index == -1:
            self.__index = self.__index + 2
            self.__reverse = False
        return self.__color_position_list[self.__index]

    def __next_position_set(self, next_color):
        Colors.validate(next_color)
        current_color_position = self.__color_position_list[self.__index]
        next_color_position = self.__color_position_map[next_color]
        if 1 == abs(current_color_position.get_position() - next_color_position.get_position()):
            self.__index = self.__color_position_list.index(next_color_position)
            return next_color_position
        else:
            message = "This color position cannot be switched {}".format(next_color_position)
            raise Exception(message)


class TrafficLights:

    def __init__(self):
        self.__color_switch = ColorSwitcher()

    def switch_to(self, color):
        return self.__color_switch.next_color(next=color)

    def switch(self):
        return self.switch_to(None)


traffic_lights = TrafficLights()

if __name__ == '__main__':
    while True:
        user_color = input("1.\tPlease insert (enter to exit) color name:")
        try:
            if len(user_color) == 0:
                break
            elif user_color.lower().__contains__('next'):
                print(traffic_lights.switch())
            else:
                print(traffic_lights.switch_to(user_color))
        except Exception as e:
            print(e)


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого
# для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Params:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_массу_асфальта(self, param):
        return self._length * self._width * param.weight * param.height


print("2.\tНапример: 20м * 5000м * 25кг * 5см = {}".format(Road(20, 5000).calculate_массу_асфальта(Params(25, 5))))


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 3. Реализовать базовый класс Worker (работник), в котором определить
# атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать
# методы экземпляров).
class Worker:
    def __init__(self, name, surname, position):
        self._name = name
        self._surname = surname
        self._position = position
        self.__income = {"wage": 1000, "bonus": 1200}

    def _get_income(self):
        return self.__income["wage"] + self.__income["bonus"]


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return self._name + " " + self._surname

    def get_income(self):
        return self._get_income()


p = Position("Alex", "Nazimov", "std")
print("3.\tPosition {} {}".format(p.get_full_name(), p.get_income()))


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

        self.go()
        self.stop()
        self.turn('left')
        self.show_speed()
        print(json.JSONEncoder().encode(jsons.dump(self)))

    def go(self):
        print("4.\tCar is going")

    def stop(self):
        print("4.\tCar is stopping")

    def turn(self, direction):
        print("4.\tCar is turning to {}".format(direction))

    def show_speed(self):
        print(f"4.\tspeed = {self._speed}")


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self._speed > 60: print("4.\tSpeed is to high: {}".format(self._speed))


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self._speed > 40: print("4.\tSpeed is to high: {}".format(self._speed))


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


TownCar(40, 'back', 'x')
TownCar(100, 'white', "t")
SportCar(120, 'yellow', 's')
SportCar(100, 'brown', 's2')
WorkCar(33, 'white', 'sc')
PoliceCar(44, "white", 'sc2')


# ---------------------------------------------------------------------


# -------------------------------------------------------------------
# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить
# в нем атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.
class Stationary():
    def __init__(self, title):
        self._title = title

    def paint(self):
        print("5. Painting start {}".format(self._title))


class Pen(Stationary):
    def __init__(self):
        super().__init__('pen')

    def paint(self):
        print("5. Painting start {}".format(self._title))


class Pencill(Stationary):
    def __init__(self):
        super().__init__('pencil')

    def paint(self):
        print("5. Painting start {}".format(self._title))


class Handle(Stationary):
    def __init__(self):
        super().__init__('handle')

    def paint(self):
        print("5. Painting start {}".format(self._title))


[element.paint() for element in [Stationary("stationary"), Pen(), Pencill(), Handle()]]
# ---------------------------------------------------------------------
