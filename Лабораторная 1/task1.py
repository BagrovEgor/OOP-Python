# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Car:
    def __init__(self, wheel_size: int, amount_doors: int):
        """
        Создание и подготовка к работе объекта "Машина"

        :param wheel__size: размер колеса
        :param amount_doors: количество дверей

        Примеры:
        >>> car = Car(17, 4)
        """
        if not (isinstance(wheel_size, int) and isinstance(amount_doors, int)):
            raise TypeError
        self.wheel_size = wheel_size
        self.amount_doors = amount_doors

    def car_going(self, speed: int):
        """
        Функция движения машины с определенной скоростью

        :param speed: скорость машины

        Пример:
        >>> car = Car(17,4)
        >>> car.car_going(300)
        """
        ...

    def car_parking(self):
        """
        Функция парковки машины

        Пример:
        >>> car = Car(17,4)
        >>> car.car_parking()
        """
        ...

class House:
    def __init__(self, smart: bool, things: list[str]):
        """
        Создание и подготовка к работе объекта "Дом"

        :param smart: является ли дом умным
        :param things: какие вещи находятся в доме

        Примеры:
        >>> house = House(False, ["beds", "chairs", "tables"])
        """
        if not (isinstance(smart, bool) and isinstance(things, list)):
            raise TypeError
        self.smart = smart
        self.things = things

    def light(self):
        """
        Функция включения света в доме

        Примеры:
        >>> house = House(False, ["beds", "chairs", "tables"])
        >>> house.light()
        """
        ...

    def сlose_curtains(self):
        """
        Функция закрытия штор

        Примеры:
        >>> house = House(False, ["beds", "chairs", "tables"])
        >>> house = house.сlose_curtains()
        """
        ...

class Computer:
    def __init__(self, characteristics: dict[str, str], cost: int):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param characteristics: характеристики компьютера
        :param cost: стоимость компьютера

        Примеры:
        >>> computer = Computer({"proc": "intel", "RAM": "16", "Disk": "SSD"}, 70000)
        """
        if not (isinstance(characteristics, dict) and isinstance(cost, int)):
            raise TypeError
        self.characteristics = characteristics
        self.cost = cost

    def calc_sum(self, a: int, b: int) -> int:
        """
        Функция вычисления суммы двух целых чисел

        :param a: певрый аргумент сложения
        :param b: второй аргумент сложения

        :return: результат целочисленного сложения

        Примеры:
        >>> computer = Computer({"proc": "intel", "RAM": "16", "Disk": "SSD"}, 70000)
        >>> computer.calc_sum(5, 6)
        """
        ...

    def click_item(self, x: float, y: float):
        """
        Выбор элемента на экране компьютера

        :param x: позиция по оси X
        :param y: позиция по оси Y

        Примеры:
        >>> computer = Computer({"proc": "intel", "RAM": "16", "Disk": "SSD"}, 70000)
        >>> computer.click_item(2.75, 3.90)
        """
        ...


if __name__ == "__main__":
    '''
    car = Car(17, 4)
    print(car.wheel_size, car.amount_doors)
    car.car_going(70)
    car.car_parking()

    house = House(False, ["beds", "chairs", "tables"])
    print(house.smart, house.things)
    house.light()
    house.сlose_curtains()

    computer = Computer({"proc": "intel", "RAM": "16", "Disk": "SSD"}, 70000)
    print(computer.characteristics, computer.cost)
    computer.calc_sum(5, 6)
    computer.click_item(2.75, 3.90)
    '''
    doctest.testmod()
