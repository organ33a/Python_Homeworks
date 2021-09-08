# Приведенный пример кода выведет на консоль тип данных переменной x, какой это будет тип? (ответ в комментах)

x = 5
print(type(x))                          # int

x = "Hello World"
print(type(x))                          # str

x = 20.5
print(type(x))                          # float

x = ["apple", "banana", "cherry"]       # list
print(type(x))

x = ("apple", "banana", "cherry")       #tuple
print(type(x))

x = {"name" : "John", "age" : 36}       #dict
print(type(x))

x = True                                # boolean
print(type(x))

# ----------------------------------------------------
# У вас есть приведенный ниже код.Восстановите пропущенную строку(...), чтобы в результате выполнения
# кода на консоли появилось указанное сообщение

x = 5
# x = x * 1.0 --- как вариант
x = float(x)
print(x, type(x))
# 5.0 <class 'float'>

x = 5
# ... ----- x изначально int, ничего не требуется
print(x, type(x))
# 5 <class 'int'>

# ----------------------------------------------------
# Воспользуйтесь методом len(), чтобы определить длину строки
x = "Hello World"
print("The lenght of our string is " + str(len(x)) + " symbols")         # 11 символов

# # Выведите на консоль первый символ строки txt.
txt = "Hello World"
x = txt[0]
print("The first symbol is -", x)



# # Напишите программу, которая выводит на консоль символы фразы "Hello World" со второго по пятый включительно.
txt = "Hello World"
print("Symbols from second to fifth are - ", txt[1:5])


# # Даны две строки "Hello World" и  " Hello World ".
# Используя переменные проверьте эти строки эквивалентны или нет.
# Если нет, преобразуйте вторую строку так, чтобы она была эквивалентна первой и убедитесь в этом.
#
txt1 = "Hello World"
txt2 = " Hello World "

# if txt1 == txt2:
#     print("The strings are equal")
# else:
#     txt2 = txt2.strip()



# Преобразуйте строку  "Hello World" так, чтобы она выводилась на консоль заглавными буквами
my_str = "Hello World"
print(my_str.upper())


# Преобразуйте строку  "Hello World" так, чтобы она выводилась на консоль строчными буквами
my_str = "Hello World"
print(my_str.lower())


# Напишите программу, которая заменит в строке "Hello World" букву H на букву J.
my_str = "Hello World"
my_str = my_str.replace("H", "J")
print("Замена произведена и вот результат - " + my_str)


# Напишите программу, которая преобразует строку "Hello World" в строку "Hello Word"
#




# У вас есть переменная my_age. Присвойте ей значение и напишите программу, которая выведет на консоль сообщение,
# в котором вместо многоточия будет значение переменной. Возраст может быть произвольным. ;-)
# I am … years old.

my_age = 20
print("I am" + " " + str(my_age) + " " + "years old.")



# Напишите программу, которая выведет на консоль сообщение, в котором вместо многоточия будет случайное значение.
# Запустите программу не менее пяти раз, чтобы убедиться, что значение случайное.
# I made this mistake … times.

import random
print("I made this mistake " + str(random.randrange(1, 10)) + " times")
