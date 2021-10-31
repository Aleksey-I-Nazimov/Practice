

# -------------------------------------------------------------------
# 1. Поработайте с переменными, создайте несколько, выведите
# на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран

my_first_var = 'Hello world'
print(my_first_var)

int_number = int(input("1. Please insert an integer number: "))
float_number = float(input ("1. Please insert a float number: "))
print("1. You inserted: {} and {}".format(int_number,float_number))
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
user_seconds = int(input ("2. Please enter seconds: "))
seconds_per_hour = 3600.0
hours = int(user_seconds // seconds_per_hour)
minutes_per_hour = 60.0
minutes = int((user_seconds % seconds_per_hour) // minutes_per_hour)
seconds = int((user_seconds % seconds_per_hour) % minutes_per_hour)

print("2. {}:{}:{}".format(hours,minutes,seconds))
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

input_number = input("3. Insert int number")
counter = 0
limit = 3
string_number = ''
new_number = 0
equation_string = ''
while True:
    string_number = string_number + input_number
    equation_string = equation_string + string_number
    print('Delta = {}'.format(string_number))
    new_number = new_number + int(string_number)
    print(" Calculating {}".format(new_number))
    counter = counter+ 1
    if counter >= limit:
        equation_string = equation_string+ '='
        break
    else :
        equation_string = equation_string + '+'
print("3. Result: "+equation_string+'{}'.format(new_number))
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# 4. Пользователь вводит целое положительное число. Найдите самую
# большую цифру в числе. Для решения используйте цикл while и
# арифметические операции
user_big_number = int(input("4. Insert an integer number: "))
comparator = 0
k = 10
xtr = 1
while True:
    xtr = xtr * k
    x_1 = user_big_number // xtr
    x_2 = user_big_number % xtr
    if x_2 < k:
        if comparator < x_2:
            comparator = x_2
    elif x_2 > k:
        v = x_2//(xtr//k)
        if comparator < v:
            comparator = v

    if x_1 < k:
        if comparator < x_1:
            comparator = x_1
    if x_1 == 0 :
        break

print("4. The biggest digit {}".format(comparator))


# -------------------------------------------------------------------
# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль
# — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчете на одного сотрудника.

income = float(input("5.Please insert your financial income: "))
outcome = float (input("5.Please insert your financial outcome: "))
if income >= outcome:
    k = income / outcome
    emp = int(input("5.Please insert the number of employers: "))
    income_per_emp = income/emp
    print('i/o = {}, income per emp = {}'.format(k,income_per_emp))
else:
    print("5.Outcome is higher than income!")
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат
# на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно
# натуральное число — номер дня

first_day = float(input("6. Please insert the result of the first day: "))
finish = float(input("6. Please insert the final distance: "))
result = 0
coef = 0.1
cnt = 0
while True:
    if result<first_day :
        result = first_day
    else:
        result = result + coef*result
    cnt = cnt + 1
    print ("{} й день: {}".format(cnt,result))

    if result>=finish:
        print("6. Oтвет: на {}й день спортсмен достиг результата - не менее {} км".format(cnt,finish))
        break

# ---------------------------------------------------------------------------------------







