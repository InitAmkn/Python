'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

'''
from random import randint


def generation_random_lst(n):
    lst = []
    for i in range(1, n+1):
        lst.append(randint(0, 9))
    return lst


def sum_numbers_with_odd_indexes(lst):
    sum = 0
    for i in range(0, len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    return sum


lst = generation_random_lst(6)
#lst = [2, 3, 5, 9, 3]
print(lst)
print(sum_numbers_with_odd_indexes(lst))
