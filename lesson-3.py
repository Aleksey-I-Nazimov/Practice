# ---------------------------------------------------------------------
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль
def dividing(value, divider):
    if divider == 0:
        message = "Value = {} Divider = {}. Zero division is not determined by math".format(value, divider)
        raise ZeroDivisionError(message)
    else:
        return value / divider


print("1.   2/4={}".format(dividing(2, 4)))
print("1.   2.01/4={}".format(dividing(2.01, 4)))
print("1.   2/4.00001={}".format(dividing(2, 4.0001)))
print("1.   0/4={}".format(dividing(0, 4)))
print("1.   1/0.00000000000000001={}".format(dividing(1, 0.00000000000000001)))
try:

    dividing(2, 0)
except ZeroDivisionError as error:
    print("1. Error was raised: message= '{}'".format(error))


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 2. Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def user_info_printer(name, surname, birth_date, city, email, tel):
    print(f"2. Name={name}, Surname={surname},"
          f" Birth date={birth_date}, City={city}, Email={email}, Tel={tel}")
    return


def user_info_printer2(**params):
    user_info_printer(params.get('name'),
                      params.get('surname'),
                      params.get('birth_date'),
                      params.get('city'),
                      params.get('email'),
                      params.get('tel'))

    return


user_info_printer("Alex", "Nazimov", "01.01.1901", "Ekaterinoslavl", "alex@alex.ru", "999-777-111")
user_info_printer2(name="Alex", surname="Nazimov",birth_date="01.01.1901",
                   city="Ekaterinoslavl", email="alex@alex.ru",tel= "999-777-111")


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(arg1, arg2, arg3):
    sorted_arg_list = sorted([arg1, arg2, arg3], reverse=True)
    return sorted_arg_list[0] + sorted_arg_list[1]


print("3. Inserted 1,2,3. Max sum = {}".format(my_func(1, 2, 3)))


# -------------------------------------------------------------------


# -------------------------------------------------------------------
# 4. Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в
# степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без
# встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def module(x):
    if x < 0.0:
        return -1.0 * x
    else:
        return x


def simple_pow(powered, n):
    result = 1
    if n >= 0:
        for i in range(0, n):
            result *= powered
        return result
    else:
        return 1.0 / simple_pow(powered, module(n))


def factorial(value):
    int_value = int(value)
    if int_value == 0:
        return 1
    elif int_value < 0:
        message = "Negative value {}".format(int_value)
        raise ValueError(message)
    else:
        return factorial(value - 1) * value


def ln(x):
    if x <= 0.0:
        message = "Illegal argument = {}".format(x)
        raise ValueError(message)
    eps = 0.0000000000000001
    series_sum = 0.0
    cnt = 1
    while True:
        coefficient = dividing(simple_pow((x - 1) / (x + 1), cnt), cnt)
        if module(coefficient) < eps:
            break
        else:
            series_sum += coefficient
            cnt += 2
    return 2 * series_sum


def teylor_pow(a, x):
    eps = 0.00000000000000001
    cnt = 1
    series_sum = 1.0
    ln_a = ln(a)
    while True:
        coefficient = simple_pow(x * ln_a, cnt) / factorial(cnt)
        if module(coefficient) < eps:
            break
        else:
            series_sum += coefficient
            cnt += 1
    return series_sum


# Задача была не использовать стандартную степень и возможно использовать цикл
# Были использованы ряды с циклами, которые дали возможность вообще ничего
# не использовать из стандартных вычислений
def my_func(x, y):
    return teylor_pow(x, y)


print("4. math.pow(1,-1)={}".format(my_func(1, -1)))
print("4. math.pow(2,-1)={}".format(my_func(2, -1)))
print("4. math.pow(2,-2)={}".format(my_func(2, -2)))
print("4. math.pow(3,-2)={}".format(my_func(3, -2)))
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 5. Программа запрашивает у пользователя строку чисел, разделенных
# пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и
# снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.
exit_code = "s"
exit_flag = False
summa = 0.0
while not exit_flag:
    user_string = input("5. Insert sth for calculating the sum: ")
    user_sub_strings = user_string.split(" ")
    max_cnt = len(user_sub_strings)
    show_result = True
    for cnt in range(0, max_cnt):
        if exit_code == user_sub_strings[cnt]:
            print("5. The stop code was read. Exiting....")
            if cnt < max_cnt - 1 or max_cnt == 1:
                show_result = False
            exit_flag = True
            break
        else:
            summa += float(user_sub_strings[cnt])
    if show_result:
        print("5. Summa = {}".format(summa))


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 6. Реализовать функцию int_func(), принимающую слово из маленьких
# латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка
# из слов, разделенных пробелом. Каждое слово состоит из латинских
# букв в нижнем регистре. Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы. Необходимо использовать
# написанную ранее функцию int_func().
def int_func(string):
    length = len(string)
    if length > 0:
        return string[0].upper() + string[1:length]
    else:
        return ""


def int_func2(string):
    separator = " "
    sub_strings = string.split(separator)
    new_string = ""
    for sub_string in sub_strings:
        new_sub_string = int_func(sub_string)
        new_string = new_string + new_sub_string + separator
    return new_string


print("6. int_func('xxxxx')={}".format(int_func("xxxxx")))
print("6. int_func2('xxxx yyyy zzzz')={}".format(int_func2('xxxx yyyy zzzz')))
# ---------------------------------------------------------------------
