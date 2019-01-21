
__author__ = 'Цапок Кристина Сергеевна'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.

x = int(input("Введите число:"))
y = x % 10
x = x // 10
while x > 0:
    if x % 10 > y:
        y = x % 10
    x = x // 10
print(y)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.

x = input("Введите текст:")
y = input("Введите текст 2:")
print(y + " " + x)



# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("ax**2 + bx + x = 0")
a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
x = int(input("Введите число x:"))
d = (b**2) - (4*a*x)
if (d < 0):
    print ("Корней нет")
elif (d > 0):
    import math
    d = math.sqrt(d)
    x1 = ((-b) + d) / (2 * a)
    x2 = ((-b) - (d)) / (2 * a)
    print("Первый корень = ", x1)
    print("Второй корень = ", x2)
else:
    x1 = -b / (2 * a)
    print("Один корень = ", x1)
