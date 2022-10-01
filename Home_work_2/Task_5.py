'''
Задание 5 Реализуйте алгоритм перемешивания списка.
'''

from random import randint


def generation_lst_N(n):
    lst = []
    for i in range(-n, n+1):
        lst.append(i)
    return lst


def random_your_list(lst):
    x = 0
    for i in range(len(lst)):
        x = randint(0, len(lst) - 1)
        #temp = lst[i]
        #lst[i] = lst[x]
        #lst[x] = temp
        lst[i], lst[x] = lst[x], lst[i]
    return lst


lst = generation_lst_N(int(input("Введите N: ")))
print(lst)


print(random_your_list(lst))
