'''
1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    - Для N = 5: 1, -3, 9, -27, 81
'''


def N_sequence(N):
    pos = []
    num = 1
    for i in range(N):
        pos.append(num)
        num = num*-3
    return pos


print(N_sequence(5))
