import random
from datetime import datetime

# Дан лист
# fruits = ["apple", "cherry", "orange", "kiwi", "melon", "banana",  "mango"]
#
# Напишите программу, которая распечатывает второй элемент листа
# print(fruits[1])
#
# # Напишите программу, которая распечатывает случайный элемент листа
#  print(fruits[random.randint(0, len(fruits)-1)])
#
# # Напишите программу, которая распечатывает элементы листа со второго по четвертый включительно
# i = 0
# while i < 7:
#     if i in [1, 2, 3]:
#         print(fruits[i])
#     i += 1
#
# # Напишите программу, которая отсортирует лист по алфавиту, после чего заменит "cherry" на "lemon" и распечатает новый лист
# fruits.sort()
# print("Отсортированный лист - ", fruits)
# name_fruit = "cherry"
# if name_fruit in fruits:
#     fruits[fruits.index(name_fruit)] = "lemon"
# print('Новый список контактов выглядит так: \n{0}'.format(fruits))

# Напишите программу, которая добавит элемент "lemon" к листу последним и распечатает новый лист
# fruits.append("lemon")
# print("Дополненный список - ", fruits)

# Напишите программу, которая добавит элемент "lemon" к листу вторым и распечатает новый лист
# fruits.insert(1, "lemon")
# print("Вставили лимончик вторым: ", fruits)
#
# Напишите программу, которая удалит элемент "banana" и распечатает новый лист
# fruits.remove("banana")
# print("удалили банан: ", fruits)

# Напишите программу, которая распечатает последний элемент исходного листа и последний элемент по алфавиту.
# print("Последний элемент исходного листа - ", fruits[(len(fruits)-1)])
# fruits = sorted(fruits)
# print("Последний элемент отсортированного листа - ", fruits[(len(fruits)-1)])


# Напишите программу, которая распечатает количество элементов в листе
# print("Количество элементов в листе - ", len(fruits))
# Напишите программу, которая проверяет есть ли элемент "orange" в листе

# if "orange" in fruits:
#     print("Orange is in list")
# else:
#     print("There is no orange in this list")

# Напишите программу, которая удаляет три произвольных элемента из листа и распечатывает средний из удаленных элементов, если их расположить в алфавитном порядке.
# i = 0
# new_fruits = []
# print(fruits)
# while i < 3:
#     rand_i = random.randint(0,len(fruits)-1)
#     print(f"произвольный элемент #{i+1} - " + fruits[rand_i] + f" c индексом {rand_i}")
#     new_fruits.append(fruits[rand_i])
#     fruits.remove(fruits[rand_i])
#     i += 1
# print("Исходный лист после удаления элементов -", fruits)
# print("Новый лист из удаленных элементов - ", new_fruits)
# new_fruits = sorted(new_fruits)
# print("Средний из удаленных и отсортированных по алфавиту элементов - ", new_fruits[1])


# Дан словарь
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1966
# }

# Напишите программу, которая изменит год выпуска на текущий
# car["year"] = datetime.now().strftime('%Y')
# # current_year_full = datetime.now().strftime('%Y') // выводит текущий год
# print("Год выпуска изменен на", car["year"])

# Напишите программу, которая добавит информацию о цвете машины и присвойте значение цвета “red”
# car["colour"] = "red"
# print(car)

# Напишите программу, удаляющую информацию о модели автомобиля
# del car["model"]
# print(car)

# Напишите программу, удаляющую всю информацию из словаря.
# car.clear()
# print("car =", car)

# Напишите программу создающую список автомобилей в Вашем гараже (не меньше трех) (возможно вымышленном).
# Для каждого автомобиля должна храниться следующая информация: марка, модель, цвет, год выпуска.
# Программа должна распечатать цвет самой старой машины.
# car1 = {
#     "name": "FW",
#     "model": "Tiguan",
#     "colour": "red",
#     "year": 2000
# }
# car2 = {
#     "name": "Audi",
#     "model": "A6",
#     "colour": "blue",
#     "year": 2000
# }
# car3 = {
#     "name": "Toyota",
#     "model": "Corolla",
#     "colour": "white",
#     "year": 2012
# }
# my_garage = [car1, car2, car3]
# min = 9999
# another_oldest_colour = ""
# for car in my_garage:
#     if car["year"] < min:
#         min = car["year"]
#         oldest_colour = car["colour"]
#     else:
#         if car["year"] == min:
#             another_oldest_colour = car["colour"]
#
# print(oldest_colour, another_oldest_colour)


# Дан лист
fruits = ["apple", "cherry", "orange", "kiwi", "melon", "banana",  "mango"]
#
# Напишите программу, которая возьмет произвольное целое число от 0 до 10 и напечатает "It is long list",
# если в листе больше элементов, чем выбранное случайное число.
# if len(fruits) > random.randint(0, 10):
#     print("It is long list")

# Напишите программу, которая возьмет произвольное целое число от 0 до 10 и напечатает "Hello World",
# если число элементов в листе не равно выбранному случайному числу.
# if len(fruits) != random.randint(0, 10):
#     print("Hello World")

# Напишите программу, которая возьмет произвольное целое число от 0 до 10 и напечатает "Yes",
# если число элементов в листе равно выбранному случайному числу, а если нет, распечатает “No”.
# if len(fruits) == random.randint(0, 10):
#     print("Yes")
# else:
#     print("No")

# Напишите программу, которая возьмет произвольное целое число от 0 до 10 и напечатает "Bingo",
# если число элементов в листе равно выбранному случайному числу,
# "It is long list", если в листе больше элементов и “It is short list” если элементов меньше.
# x = random.randint(0, 10)
# if len(fruits) == x:
#     print("Bingo")
# elif len(fruits) > x:
#     print("It is long list")
# else:
#     print("It is short list")

# Заданы четыре числа a, b, c и d. Напишите программу, которая "Great equality", если a равно b и с равно d.
# А в противном случае программа напечатает “Oops!”
# a, b, c, d = 3, 3, 123, 12
# if a == b and c == d:
#     print("Great equality")
# else:
#     print("Oops!")


# Напишите программу, которая создаст лист из четырех произвольных целых чисел от 0 до 10 и печатает "Success",
# если первый элемент больше последнего или второй элемент больше третьего.
# Если ни одно из условий не выполнено, то программа печатает “Failure”
# my_list = []
# for i in range(4):
#     x = random.randint(0, 10)
#     my_list.append(x)
# print(my_list)
# if my_list[0] > my_list[3] or my_list[1] > my_list[2]:
#     print("Success")
# else:
#     print("Failure")

# Напишите программу, которая создаст лист из семи произвольных целых чисел от 0 до 10 и печатает "Success",
# если третий элемент листа больше первого и меньше последнего.
# Если ни одно из условий не выполнено, то программа печатает “Failure”
# my_list = []
# for i in range(7):
#     x = random.randint(0, 10)
#     my_list.append(x)
# print(my_list)
# if my_list[2] > my_list[0] and my_list[2] < my_list[len(my_list)-1]:
#     print("Success")
# else:
#     print("Failure")

# Напишите программу, которая печатает произвольные числа в диапазоне от 0 до 20 до тех пор,
# пока значение случайного числа не станет меньше 3.
# Пусть программа напечатает сообщение, чему равно число из-за которого она прекратила выполнение.
# x = random.randint(0, 20)
# while x >= 3:
#     x = random.randint(0,20)
#     print(x)
# print(f"программа завершена, т.к. х стал меньше 3 и равен {x}")

# Напишите программу, которая выбирает произвольное целое число в диапазоне от 5 до 15, а затем печатает
# последовательность чисел от 1 до 20 (включительно) за исключением выбранного числа.
# x = random.randint(5, 15)
# print("random x is ", x)
# i = 0
# while i < 20:
#     i += 1
#     if i == x:
#         continue
#     print(i)

# Print a message once the condition is false
#
# Дан лист
fruits = ["apple", "cherry", "orange", "kiwi", "melon", "banana",  "mango"]
#
# Напишите программу, которая выведет каждый элемент отдельно, за исключением “banana”
# for i in fruits:
#     if i == "banana":
#         continue
#     print(i)


#
# Напишите программу, которая будет печатать все фрукты, пока не дойдет до “kiwi”. А затем прекратит работу.
# for i in fruits:
#     if i == "kiwi":
#         break
#     print(i)
#
# Напишите функцию my_sum, которая принимает два параметра и возвращает их сумму
# def my_sum(a, b):
#     c = a + b
#     return c
#
#
# print("Введите первое число")
# x = int(input())
#
# print("Введите второе число")
# y = int(input())
#
# print("SUM = ", my_sum(x, y))


# Напишите функцию my_new_sum, которая принимает любое число параметров и возвращает их сумму.
# def my_new_sum(*nums):
#     sum = 0
#
#     for n in nums:
#         sum += n
#
#     print("Sum: ", sum)
#
#
# my_new_sum(3, 5)
# my_new_sum(4, 5, 6, 7)
# my_new_sum(1, 2, 3, 5, 6)

# Напишите программу, в которой есть функция, принимающая перечень людей с указанием их возраста и возвращающая возраст самого старшего.
def the_oldest_bubble (*args, age_key):
    ages = []
    print(len(args))
    age_curr = args[0][age_key]
    # bubble sort
    for i in args:
        if i[age_key] > age_curr:
            print(i[age_key])
            ages = i
    return ages


persons=[]
person = {
    "First Name": "Alex",
    "Last Name":  "Popov",
    "Age": 68
    }
persons.append(person)

person = {
    "First Name": "Elena",
    "Last Name":  "Boden",
    "Age": 45
    }
persons.append(person)

person = {
    "First Name": "Jack",
    "Last Name":  "Little",
    "Age": 25
    }
persons.append(person)

person={
    "First Name": "Nina",
    "Last Name":  "McDonald",
    "Age": 80
    }
persons.append(person)

print(persons)
print(the_oldest_bubble(*persons, age_key="Age"))


# Видоизмените программу из предыдущего задания, так чтобы программа случайным образом выбирала самого старшего или самого младшего. При этом указывала выбранный возраст это минимальный или максимальный.

random_bool=random.randint(0,1)
print(f"Random Boolean:{random_bool}")
if random_bool:
    print("The max age is: ")
else:
    print("The min age is:")
persons_sorted_by_age=sorted(persons, key=lambda k : k['Age'], reverse=random_bool)
print(persons_sorted_by_age[0])