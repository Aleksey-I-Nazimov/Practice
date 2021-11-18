# ---------------------------------------------------------------------
# 1. Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# свидетельствует пустая строка.
# environment vars: PYTHONIOENCODING=utf-16

# reading user data:---------------------------------------------------
import sys

system_file_encoding = sys.getdefaultencoding()
print("1\tSystem preferred encoding {}".format(system_file_encoding))
user_input_cache = list()
corp_counter = 0
while True:
    corp_counter += 1
    user_line = input(f"{corp_counter}. Please insert something:")
    if len(user_line) > 0:
        user_input_cache.append(user_line)
    else:
        break
print("1.\tStrings inserted by user: {}".format(user_input_cache))

# writing user data:---------------------------------------------------
read_file = "user_strings.txt"
try:
    read_file = open(read_file, "w", encoding=system_file_encoding)
    # The first approach:
    for user_string in user_input_cache:
        read_file.write(user_string + "\n")
    # The second approach:
    # read_file.writelines(user_input_cache)
except Exception as e:
    print("IO exception: {}".format(e))
finally:
    read_file.close()
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
read_file = "user_strings.txt"
try:
    with  open(read_file, "r", encoding=system_file_encoding) as read_file:
        read_lines = read_file.readlines()
    string_counter = 0
    for read_line in read_lines:
        string_counter += 1
        string_words = len([e for e in read_line.split(" ") if len(e) > 0])
        print(f"2.\tВ строке {string_counter} записано {string_words} слов-о/а")
    print(f"2.\tВсего строк {string_counter}")
except Exception as e:
    print("IO exception: {}".format(e))
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
salary_threshold = 20000
read_file = "salary.txt"
poor_list = []
average_person_profit = 0.0
person_counter = 0

try:
    with open(read_file, "r", encoding=system_file_encoding) as read_file:
        read_lines = read_file.readlines()

        for read_line in read_lines:
            values = read_line.split(" ")
            surname = str(values[0])
            salary = float(values[1])
            average_person_profit += salary
            person_counter += 1
            print(f"3.\t{corp_counter} Mr. {surname} salary={salary}")
            if salary <= salary_threshold: poor_list.append(surname)

except Exception as e:
    print("IO exception: {}".format(e))

print(f"3.\tAverage salary {(average_person_profit / (person_counter - 1))}")
print(f"3\tPersons: {poor_list} which don't earn more than {salary_threshold}")
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.
read_file = "nums.txt"
output_file = "output_nums.txt"
dictionary = {"One": "Oдин", "Two": "Два", "Three": "Три", "Four": "Четыре"}
splitter = " - "

try:
    with open(read_file, "r", encoding=system_file_encoding) as read_file:
        read_lines = read_file.readlines()
        with open(output_file, "w", encoding=system_file_encoding) as output_file:
            for read_line in read_lines:
                values = read_line.split(splitter)
                translated_value = dictionary[values[0]]
                new_line = translated_value + splitter + values[1]
                output_file.write(new_line)
            output_file.flush()

except Exception as e:
    print("IO exception: {}".format(e))
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 5. Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить ее на экран.
from functools import reduce

nums = [str(element) for element in range(0, 10)]
output_string = ""
delimiter = " "
limit = len(nums)
for index in range(0, limit):
    output_string += nums[index]
    if index < (limit - 1):
        output_string += delimiter
with open("splitted_nums.txt", "w", encoding=system_file_encoding) as o: o.write(output_string)
with open("splitted_nums.txt", "r", encoding=system_file_encoding) as r:
    print(f'5.\t∑={reduce(lambda n1, n2: n1 + n2, [float(num) for num in r.readline().split(delimiter)])}')
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

num_parser = lambda v: int(v)
none_parser = lambda v: 0
hour_types = {"(л)": num_parser, "(пр)": num_parser, "(лаб)": num_parser, "-": none_parser}
delimiter = ": "
space_delimiter = " "


def discipline_work_plan_calc(data):
    data_list = data.split(space_delimiter)
    data_map = {}
    for hour_key in hour_types.keys():
        for data_element in data_list:
            if data_element.find(hour_key) >= 0:
                data_map[hour_key] = hour_types[hour_key](data_element.split(hour_key)[0])
    return reduce(lambda n1, n2: n1 + n2, data_map.values())


output_map = {}
with open("learning_plan.txt", "r", encoding=system_file_encoding) as r:
    learning_plan_lines = r.readlines()
    for learning_plan_line in learning_plan_lines:
        discipline_data = learning_plan_line.split(delimiter)
        output_map[discipline_data[0]] = discipline_work_plan_calc(discipline_data[1])
    print(f"6.\t{output_map}")
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 7. Создать (не программно) текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности,
# выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка:
# [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

corp_file = "corp.txt"
all_corps = []
with open(corp_file, "r", encoding=system_file_encoding) as corp_file:
    corp_list = corp_file.readlines()
    average_profit = 0.0
    corp_counter = 0
    for corp in corp_list:
        corp_elements = corp.split(" ")
        name = corp_elements[0]
        profit = float(corp_elements[2]) - float(corp_elements[3])
        all_corps.append({name: profit})
        if profit >= 0:
            average_profit += profit
            corp_counter += 1
    all_corps.append({"average_profit": (average_profit / (corp_counter - 1))})

print(f"7.\t{all_corps}")

import json

corp_file = "corp_results.txt"
with open(corp_file, "w", encoding=system_file_encoding) as corp_file:
    json.dump(all_corps, corp_file)
# ---------------------------------------------------------------------
