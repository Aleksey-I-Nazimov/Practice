# ---------------------------------------------------------------------
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода
# матрицы в привычном виде. Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица. Подсказка: сложение элементов
# матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.
def assert_array(elements):
    if not isinstance(elements, type([])):
        raise Exception("The input argument has to be an array")
    return elements


class Vector:

    def __init__(self, elements):
        self.coordinates = []
        self.coordinates.extend(assert_array(elements))

    def size(self):
        return len(self.coordinates)

    def __getitem__(self, item):
        return self.coordinates[item]

    def __add__(self, vector):
        if not isinstance(vector, type(Vector([]))): raise Exception("Non vector argument is not allowed")
        if vector.size() != self.size(): raise Exception("Vectors has different sizes")
        return Vector([self[index] + vector[index] for index in range(0, self.size())])

    def __str__(self):
        bracket = "|"
        delimiter = "\t"
        str = "" + bracket
        size = len(self.coordinates)
        for index in range(0, len(self.coordinates)):
            str += f"{self.coordinates[index]:.3f}"
            if index < size - 1:
                str += delimiter
            else:
                str += bracket
        return str


class Matrix:

    def __init__(self, matrix_elements):
        self.vectors = []
        size_control = -1
        for matrix_vector in matrix_elements:
            if isinstance(matrix_vector, type(Vector([]))):
                new_vector = matrix_vector
            else:
                new_vector = Vector(matrix_vector)
            self.vectors.append(new_vector)
            if size_control == -1: size_control = new_vector.size()
            if size_control != new_vector.size():
                message = "The new vector is has illegal size value = {}".format(new_vector.size())
                raise Exception(message)

        self.column_number = size_control
        self.row_number = len(self.vectors)

    def get_columns(self):
        return self.column_number

    def get_rows(self):
        return self.row_number

    def __getitem__(self, item):
        return self.vectors[item]

    def __add__(self, other):
        if not isinstance(other, type(Matrix([]))): raise Exception("Only matrix class can be add")
        new_vectors = []
        for index in range(0, self.get_rows()):
            new_vectors.append(self[index] + other[index])
        return Matrix(new_vectors)

    def __str__(self):
        xtr = ""
        for vector in self.vectors:
            xtr += vector.__str__()
            xtr += "\n"
        return xtr


m1 = Matrix([[1, 2, 3], [5, 6, 7]])
m2 = Matrix([[3, 2, 1], [7, 6, 5]])

print("1.\tСложение матриц\n{}+\n{}=\n{}".format(m1, m2, m1 + m2))
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 2. Реализовать проект расчета суммарного расхода ткани на
# производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.
import abc


class Clothes:

    def __init__(self, v, h):
        self.v = v
        self.h = h

    @abc.abstractmethod
    def _resource(self):
        pass

    @property
    def calculated_resource(self):
        print("Расчет затрата ткани: {}".format(type(self)))
        resource = self._resource()
        print("Будет потрачено {} m2".format(resource))
        return resource


class Coat(Clothes):

    def __init__(self, v, h):
        super().__init__(v, h)

    def _resource(self):
        return self.v / 6.5 + 0.5


class Jacket(Clothes):

    def __init__(self, v, h):
        super().__init__(v, h)

    def _resource(self):
        return 2 * self.h + 0.3


coat = Coat(5, 5)
jacket = Jacket(10, 10)

print("2.\tFor coat: {}".format(coat.calculated_resource))
print("2.\tFor jacket: {}".format(jacket.calculated_resource))
# ---------------------------------------------------------------------


# -------------------------------------------------------------------
# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать
# параметр, соответствующий количеству клеток (целое число). В классе
# должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к
# клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
# деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки
# должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
# если разность количества ячеек двух клеток больше нуля, иначе выводить
# соответствующее сообщение. Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток. Деление. Создается общая клетка из двух. Число ячеек
# общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр
# класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество
# ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда
# не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки равняется
# 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
import json
import jsons


class Cell:

    def __init__(self, number):
        self.number = number

    def __add__(self, cell):
        return Cell(self.number + cell.number)

    def __sub__(self, cell):
        sub_value = self.number - cell.number
        if sub_value >= 0:
            return Cell(sub_value)
        else:
            message = "Forbidden cell value = {}".format(sub_value)
            raise Exception(message)

    def __mul__(self, cell):
        return Cell(self.number * cell.number)

    def __truediv__(self, other):
        return Cell(int(self.number / other.number))

    def __str__(self):
        return json.JSONEncoder().encode(jsons.dump(self))

    def make_order(self, order):
        xtr = ""
        for index in range(0, self.number):
            xtr += "*"
            if (index + 1) % order == 0:
                print(xtr)
                xtr = ""
            elif index == self.number - 1:
                print(xtr)


cell1 = Cell(1)
cell2 = Cell(2)
cell4 = Cell(4)

print("3.\tSum cell {}".format(cell1 + cell2))
print("3.\tMul cell {}".format(cell2 * cell2))
print("3.\tDiv cell {}".format(cell4 / cell2))
print("3.\tDif cell {}".format(cell4 - cell1))
try:
    cell1 - cell2
except Exception as e:
    print("3.\tMessage={}".format(e))

cell8 = cell2 * cell4
print("3.\tChecking order:\n")
cell8.make_order(3)
# ---------------------------------------------------------------------
