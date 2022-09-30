'''
2. Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
    - Для n = 6: [4, 7, 10, 13, 16, 19]
'''


def N_sequence(N):
    pos = []
    i = 1
    while (i <= N):
        pos.append(3 * i + 1)
        i += 1
    return pos


print(N_sequence(6))
