
'''
Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''


def not_factorial(number):
    output_lst = []
    factorial_i = 1
    for i in range(1, number+1):
        factorial_i *= i
        output_lst.append(factorial_i)
    return output_lst


print(not_factorial(int(input("Введите число: "))))
