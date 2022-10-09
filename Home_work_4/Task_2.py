
'''
2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

*Пример*

- при N=236     ->        [2, 2, 59]

'''


def prime_factors(N):
    factors = []
    prime = 2
    while (N > prime):
        if N % prime == 0:
            factors.append(prime)
            N //= prime
        else:
            prime += 1
    if N > 1:
        factors.append(N)
    return factors


print(prime_factors(int(input())))
