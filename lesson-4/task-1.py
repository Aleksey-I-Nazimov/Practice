
# ---------------------------------------------------------------------
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета
# для конкретных значений необходимо запускать скрипт с параметрами.
# JUST RUN start-task-1.bat
from sys import argv

# Object for storing command line parameters:------------------------
script_name, time, priceTime, bonus = argv

print ("Input script args: time={}, priceTime={}, bonus={}".format(time,priceTime,bonus))
time = float(time)
priceTime = float(priceTime)
bonus = float(bonus)
salary = time*priceTime+bonus

print ("Salary = time*priceTime+bonus ={}".format(salary))

