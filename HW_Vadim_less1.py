# 1) Создать переменную типа String
my_str = "переменная типа String"

# 2) Создать переменную типа Integer
x_i = 1

# 3) Создать переменную типа Float
x_f = 1.0

# 4) Создать переменную типа Bytes
x_b = b"babayts"

# 5) Создать переменную типа List
x_lst = [1, 2, 3]

# 6) Создать переменную типа Tuple
x_tpl = (1, 2, 3)

# 7) Создать переменную типа Set
x_set = {1, 2, 3}

# 8. Создать переменную типа Frozen set
x_fr_set =frozenset({1, 2, 3})

# 9) Создать переменную типа Dict
x_dct = {"name": "Alla", "age": 56}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(my_str, type(my_str))
print(x_i, type(x_i))
print(x_f, type(x_f))
print(x_b, type(x_b))
print(x_lst, type(x_lst))
print(x_tpl, type(x_tpl))
print(x_set, type(x_set))
print(x_fr_set, type(x_fr_set))
print(x_dct, type(x_dct))

# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
str1 = "пи"
str2 = "васик"
str3 = str1 + str2
print(str3)

# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
var1 = 5
var2 = 2
var3 = var1 + var2
print("sum =", var3)

# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
var4 = var1 / var2
print("var1/var2 =", var4)

# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
var5 = var1 * var2
print("var1*var2 =", var5)

# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
var6 = var1 // var2
print("деление без остатка --", var6)

# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
var7 = var1 % var2
print("остаток от деления --", var7)
