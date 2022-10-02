

'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

'''


from random import uniform


def generation_random_lst(n):
    lst = []
    for i in range(1, n+1):
        lst.append(round(uniform(0.0, 9.9), 2))
    return lst


def fractional_parts(lst):
    lst_output = []
    for i in range(0, len(lst)):
        if lst[i] - lst[i] // 1 != 0:
            lst_output.append(round(lst[i] - lst[i] // 1, 2))
    return lst_output


def find_difference_min_max(lst):
    min = lst[0]
    max = lst[0]
    for i in range(0, len(lst)):
        if lst[i] < min:
            min = lst[i]
        if lst[i] > max:
            max = lst[i]
    return round(max - min, 2)


print("Тест с рандомным листом:")
lst = generation_random_lst(3)
print(lst)
print(fractional_parts(lst))
print(find_difference_min_max(fractional_parts(lst)))
print("Тест с листом из примера:")
lst_1 = [1.1, 1.2, 3.1, 5, 10.01]
print(lst_1)
print(fractional_parts(lst_1))
print(find_difference_min_max(fractional_parts(lst_1)))
