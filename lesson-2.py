# ---------------------------------------------------------------------
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе
list = [None, type(''), True, 1, 0.5, "string", [1, 2, 4]]
for element in list:
    print(' 1. Element = {} data type = {}'.format(element, type(element)))
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()
user_list = []
while True:
    element = input("2. Please insert the list element (NULL means exit): ")
    print("   -> read element = {}".format(element))
    if element.lower().__contains__('null'):
        break
    user_list.append(element)

cnt = 0
while cnt < len(user_list) - 1:
    user_list[cnt], user_list[cnt + 1] = user_list[cnt + 1], user_list[cnt]
    cnt += 2

for element in user_list:
    print("  --  {}".format(element))
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить
# к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
months_list = ['winter', 'winter', 'spring', 'spring', 'spring',
               'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
months_map = {0: 'winter', 1: 'winter', 2: 'spring', 3: 'spring', 4: 'spring',
              5: 'summer', 6: 'summer', 7: 'summer', 8: 'autumn', 9: 'autumn', 10: 'autumn', 11: 'winter'}

month_number = int(input("Пожалуйста введите номер месяца (1... 12): "))
if month_number < 1 or month_number > 12:
    message = "3. Month number is not in [1:12]. Current value = {}".format(month_number)
    raise RuntimeError(message)
month_number = month_number - 1
print("3. Get from list {}".format(months_list[month_number]))
print("3. Get from map {}".format(months_map[month_number]))
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
word_limit = 10
user_message = input("4. Please, insert your message: ")
user_message_words = user_message.split(" ")
cnt = 0
while cnt < len(user_message_words):
    if len(user_message_words[cnt]) < word_limit:
        print("4. # {} word message {}".format(cnt, user_message_words[cnt]))
    else:
        print("4. # {} short message {}".format(cnt, user_message_words[cnt][0:word_limit:1]))
    cnt += 1
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый
# элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.

rate_list = [7, 5, 3, 3, 2]
while True:
    element = input("5. Please insert the rate int number (NULL means exit): ")
    print("   -> read element = {}".format(element))
    if element.lower().__contains__('null'):
        break
    rate_list.append(int(element))
    rate_list.sort(reverse=True)
    print("5. Rate {} ".format(rate_list))

# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# 6. * Реализовать структуру данных «Товары». Она должна представлять собой
# список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
name_key = "название"
price_key = "цена"
number_key = "количество"
number_meas_key = "ед."
product_list = []
while True:
    key = input("6. Please insert the product key : ")
    name = input("6. Please insert the product name : ")
    price = input("6. Please insert the product price : ")
    number = input("6. Please insert the product number : ")
    number_measure = input("6. Please insert the product number measure : ")

    if key.lower().__contains__('null') or name.lower().__contains__('null') \
            or price.__contains__('null') or number.__contains__('null') or number_measure.__contains__('null'):
        print("   -> read NULL element = {}".format(element))
        break
    else:
        product_list.append(
            (key, {name_key: name, price_key: price, number_key: number, number_meas_key: number_measure}))

name_list = []
price_list = []
number_list = []
number_meas_list = []
anal_map = {name_key: name_list, price_key: price_list, number_key: number_list, number_meas_key: number_meas_list}

print("6. Product list {}".format(product_list))

for product in product_list:
    product_key = product[0]
    product_map = product[1]
    name_list.append(product_map.get(name_key))
    price_list.append(product_map.get(price_key))
    number_list.append(product_map.get(number_key))
    number_meas_list.append(product_map.get(number_meas_key))

print ("6. Product anal. map {}".format(anal_map))

# ---------------------------------------------------------------------
