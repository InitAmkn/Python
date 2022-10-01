'''
Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

6782 -> 23
0,56 -> 11
'''


def sum_numbers(number):
    m = str(number)
    sum = 0
    for i in m:
        if i.isdigit():
            sum += int(i)
    return sum


print(sum_numbers(5.24))
