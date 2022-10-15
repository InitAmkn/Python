
'''
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''
import math

# было


def not_factorial(number):
    output_lst = []
    factorial_i = 1
    for i in range(1, number+1):
        factorial_i *= i
        output_lst.append(factorial_i)
    return output_lst


n = int(input("Введите число: "))

print(not_factorial(n))

# стало
lst_ = [i for i in range(1, n+1)]
lst = list(map(lambda x: math.prod(lst_[:x]), lst_))

print(lst)
