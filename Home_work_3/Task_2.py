
'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

from random import randint


def generation_random_lst(n):
    lst = []
    for i in range(1, n+1):
        lst.append(randint(0, 9))
    return lst


def multiply_first_and_last_numbers(lst):
    lst_output = []
    if len(lst) % 2 == 0:
        len_lst_output = len(lst) // 2
    if len(lst) % 2 != 0:
        len_lst_output = len(lst) // 2 + 1
    for i in range(0, len_lst_output):
        lst_output.append(lst[i]*lst[len(lst)-i-1])
    return lst_output


lst = generation_random_lst(5)
print(lst)
print(multiply_first_and_last_numbers(lst))
