'''
3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

*Пример*

- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

'''

lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]


def list_non_repeatable(lst):
    out_lst = []
    for i in range(len(lst)):
        count = 0
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                count += 1
        for j in range(0, i):
            if lst[i] == lst[j]:
                count += 1
        if count < 1:
            out_lst.append(lst[i])
    return out_lst


def list_non_repeatable(lst):
    out_lst = []
    for i in range(len(lst)):
        count = 0
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                count += 1
        for j in range(0, i):
            if lst[i] == lst[j]:
                count += 1
        if count < 1:
            out_lst.append(lst[i])
    return out_lst


print(list_non_repeatable(lst))
