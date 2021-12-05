import json
from datetime import datetime

import jsons


# ---------------------------------------------------------------------
# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год». В рамках
# класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу
# «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.

class WrongDayException(Exception):

    def __init__(self, message):
        super().__init__(message)


class WrongMonthException(Exception):

    def __init__(self, message):
        super().__init__(message)


class WrongYearException(Exception):

    def __init__(self, message):
        super().__init__(message)


class Date:

    def __init__(self, **kwargs):
        if kwargs.get("default"):
            date_time = datetime.strptime(kwargs.get("date_time"), "%d/%m/%y")
            self.__day = date_time.day
            self.__month = date_time.month
            self.__year = date_time.year
        else:
            date_time = Date.parse_by_slash(kwargs.get("date_time"))
            self.__day = int(date_time["day"]) - 1
            self.__month = int(date_time["month"]) - 1
            self.__year = int(date_time["year"])

    def __str__(self):
        return self.__dict__.__str__()

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @staticmethod
    def parse_by_slash(string):
        if isinstance(string, type(str())):
            xtr = string.__str__().split("/")
            return {"day": xtr[0], "month": xtr[1], "year": xtr[2]}
        else:
            raise TypeError("The input argument is not a string")

    @classmethod
    def date(cls, date_string):
        default_date = Date(date_time=date_string, default=True)
        return default_date.day

    @staticmethod
    def validate(date_string):

        date_time = Date(date_time=date_string, default=False)
        day = date_time.day
        year = date_time.year
        month = date_time.month

        if 0 > day or day > 31:
            message = f"{day} wrong day value"
            raise WrongDayException(message)
        if 0 > month or month > 11:
            message = f"{month} wrong month value"
            raise WrongMonthException(message)
        if year < 0:
            message = f"{year} wrong year value"
            raise WrongYearException(message)
        print("1.\tThe date string is valid: {}".format(date_string))


try:
    date = Date.validate("-19/12/8")
except WrongDayException as e:
    print("1\tWrongDayException: ", e)

try:
    date = Date.validate('19/-12/8')
except WrongMonthException as e:
    print("1\tWrongMonthException: ", e)

try:
    date = Date.validate('19/12/-19')
except WrongYearException as e:
    print("1\tWrongYearException: ", e)

print("1.\tValid date: {}".format(Date(date_time="19/12/88", default=True)))
print("1.\tValid date: {}".format(Date(date_time="19/12/88")))
print("1.\tDay: {}".format(Date.date("19/12/88")))


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class ExceptionHandler:

    def handle(self, lambda_function):
        try:
            return lambda_function()
        except ZeroDivisionError as zero_division_error:
            print("2.\tZero division error: {}".format(zero_division_error))
        return None


value1 = float(input("2.\tВведите делимое: "))
value2 = float(input("2.\tВведите делитель: "))

print("2.\tResult = {}".format(ExceptionHandler().handle(lambda_function=lambda: value1 / value2)))


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 3. Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например,
# команду “stop”. При этом скрипт завершается, сформированный список
# выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить
# только числа и строки. При вводе пользователем очередного элемента
# необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю
# ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.
class NoneZeroReferenceException(Exception):

    def __init__(self, reference):
        super().__init__(f"The following element is not a number {reference}")


class StatefulListFactory:

    def __init__(self):
        self.__factory_list = []

    def append(self, element):
        self.__factory_list.append(float(StatefulListFactory.__control_value(element)))
        return self

    def to_list(self):
        list_copy = self.__factory_list
        self.__factory_list = None
        if list_copy is None:
            raise ReferenceError("To list method has already been executed")
        return list_copy

    @staticmethod
    def __control_value(element):
        if element is not None:
            string = element.__str__()
            if string.isdigit():
                return element
        raise NoneZeroReferenceException(element)


list_factory = StatefulListFactory()
cnt = 0
stop_code = "stop"
while True:
    cnt += 1
    xtr = input(f"3.\t{cnt} Введите число: ")
    try:
        list_factory.append(xtr)
    except NoneZeroReferenceException as zero_exception:
        if stop_code.__eq__(xtr):
            print("3.\tStop")
            break
        else:
            print(f"3.\t{cnt} Exception:{zero_exception}")

new_list = list_factory.to_list()
print(f"3.\tOutput list: {new_list}")


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого
# типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное
# подразделение компании. Для хранения данных о наименовании и количестве
# единиц оргтехники, а также других данных, можно использовать любую подходящую
# структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.
class Gadget:

    def __init__(self, firmware=None, pc_interface=None, style=None, series=None, size=None, voltage=None):
        self.__firmware = firmware
        self.__pc_interface = pc_interface
        self.__style = style
        self.__series = series
        self.__size = size
        self.__voltage = voltage

    @staticmethod
    def call_init(ref, **kwargs):
        ref.__init__(kwargs.get("firmware"), kwargs.get("pc_interface"),
                     kwargs.get("style"), kwargs.get("series"),
                     kwargs.get("size"), kwargs.get("voltage"))


class Scanner(Gadget):

    def __init__(self, **kwargs):
        Gadget.call_init(super(), **kwargs)
        self.__scanner_type = kwargs.get("scanner_type")

    def __str__(self):
        return json.JSONEncoder().encode(jsons.dump(self))


class Printer(Gadget):

    def __init__(self, **kwargs):
        Gadget.call_init(super(), **kwargs)
        self.__printer_type = kwargs.get("printer_type")
        self.__has_scanner = kwargs.get("has_scanner")

    def __str__(self):
        return json.JSONEncoder().encode(jsons.dump(self))


class Copier(Gadget):

    def __init__(self, **kwargs):
        Gadget.call_init(super(), **kwargs)
        self.__copier_type = kwargs.get("copier_type")

    def __str__(self):
        return json.JSONEncoder().encode(jsons.dump(self))


class CheckGadget:

    def __call__(self, function):
        def proxy_function(*args):
            arg = args[1]
            if not issubclass(arg.__class__, Gadget):
                message = f"{type(arg)} is not supported"
                raise TypeError(message)
            return function(*args)

        return proxy_function

    def __str__(self):
        return json.JSONEncoder().encode(jsons.dump(self))


class Store:
    PRINTER = "printer"
    SCANNER = "scanner"
    COPIER = "copier"

    def __init__(self):
        self.__printers = []
        self.__scanners = []
        self.__copiers = []
        self.__quantity = {Store.PRINTER: 0, Store.SCANNER: 0, Store.COPIER: 0}

    @CheckGadget()
    def put_printer(self, p):
        self.__printers.append(p)
        self.__quantity[Store.PRINTER] += 1
        return self

    @CheckGadget()
    def put_scanner(self, s):
        self.__scanners.append(s)
        self.__quantity[Store.SCANNER] += 1
        return self

    @CheckGadget()
    def put_copier(self, c):
        self.__copiers.append(c)
        self.__quantity[Store.COPIER] += 1
        return self

    def provide_gadget(self, consumer):
        gadget_type = consumer.get_gadget_type()
        gadget = None
        if gadget_type == Store.PRINTER:
            gadget = self.__printers.pop(len(self.__printers) - 1)
            self.__quantity[Store.PRINTER] -= 1
        elif gadget_type == Store.SCANNER:
            gadget = self.__scanners.pop(len(self.__scanners) - 1)
            self.__quantity[Store.SCANNER] -= 1
        elif gadget_type == Store.COPIER:
            gadget = self.__copiers.pop(len(self.__copiers) - 1)
            self.__quantity[Store.COPIER] -= 1
        else:
            message = "Unsupported gadget type {}".format(gadget_type)
            raise Exception(message)
        consumer.apply(gadget)
        return gadget

    def __str__(self):
        return json.JSONEncoder().encode(jsons.dump(self))


store = Store()

printer = Printer(firmware="hp", pc_interface="usb", style="gray",
                  series="smart-100", size="micro", voltage="220V", has_scanner="yes", printer_type="laser")
scanner = Scanner(firmware="media", pc_interface="usb", style="gray",
                  series="smart-105", size="miditower", voltage="220V", scanner_type="laser")
copier = Copier(firmware="xerox", pc_interface="usb", style="gray",
                series="smartx-100", size="big", voltage="220V", copier_type="xerox")

store \
    .put_copier(copier) \
    .put_scanner(scanner) \
    .put_printer(printer)

print("4.\tStore: {}".format(store))


class StorePrinterConsumer:

    def get_gadget_type(self):
        return Store.PRINTER

    def apply(self, printer):
        print(f"4.\tConsumed the new printer {printer}")


store.provide_gadget(StorePrinterConsumer())


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.

def check_complex_type(num_object):
    if not isinstance(num_object, type(Complex())):
        message = "Unsupported type {}".format(type(num_object))
        raise TypeError(message)
    return num_object


class Complex:

    def __init__(self, remum=0.0, imaginary=0.0):
        self.remum = float(remum)
        self.imaginary = float(imaginary)

    def __add__(self, num):
        other_complex = check_complex_type(num)
        return Complex(self.remum + other_complex.remum, self.imaginary + other_complex.imaginary)

    def __mul__(self, num):
        other_complex = check_complex_type(num)
        ac = self.remum * other_complex.remum
        bd = self.imaginary * other_complex.imaginary
        ad_bc = self.remum * other_complex.imaginary + self.imaginary * other_complex.remum
        return Complex(ac - bd, ad_bc)

    def __sub__(self, num):
        other_complex = check_complex_type(num)
        return Complex(self.remum - other_complex.remum, self.imaginary - other_complex.imaginary)

    def __truediv__(self, num):
        other_complex = check_complex_type(num)
        ac = self.remum * other_complex.remum
        bd = self.imaginary * other_complex.imaginary
        bc = self.imaginary * other_complex.remum
        ad = self.remum * other_complex.imaginary
        c2 = pow(other_complex.remum, 2)
        d2 = pow(other_complex.imaginary, 2)
        return Complex((ac + bd) / (c2 + d2), (bc - ad) / (c2 + d2))

    def __str__(self):
        if self.imaginary > 0:
            return f"({self.remum}+i{self.imaginary})"
        elif self.imaginary < 0:
            return f"({self.remum}-i{abs(self.imaginary)})"
        else:
            return f"{self.remum}"


c1 = Complex(4, 4)
c2 = Complex(2, 2)
print(f"5.\t{c1}+{c2}={c1 + c2}")
print(f"5.\t{c1}*{c2}={c1 * c2}")
print(f"5.\t{c1}-{c2}={c1 - c2}")
print(f"5.\t{c1}/{c2}={c1 / c2}")
# ---------------------------------------------------------------------
