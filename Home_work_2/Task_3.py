
'''
Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.

Пример:

Для n = 6 -> 14.072
'''


def calc_function(n):
    sum = 0
    for i in range(len(n)):
        sum += (1+1/n[i])**n[i]
    return round(sum, 3)


def generation_lst(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i)
    return lst


n = int(input("Введите n: "))
print(generation_lst(n))
print(calc_function(generation_lst(n)))
