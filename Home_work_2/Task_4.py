'''
Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.
'''


def generation_lst_N(n):
    lst = []
    for i in range(-n, n+1):
        lst.append(i)
    return lst


def multiply_numbers_by_indexes(a, b, lst):
    return lst[a]*lst[b]


lst = generation_lst_N(int(input("Введите N: ")))
print(lst)

a = int(input("Введите a: "))
b = int(input("Введите b: "))
print(f"{lst[a]} * {lst[b]} = ", multiply_numbers_by_indexes(a, b, lst))
