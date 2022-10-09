
'''
1 Вычислить число π c заданной точностью d

*Пример:*

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
https://completerepair.ru/kak-vychislit-chislo-pi


π = 2√3*(1 - (1/3)*(1/3) + (1/5)*(1/3)^2 - (1/7)*(1/3)^3… + 1/((2n + 1)*(-3)^n)…)
'''


def find_pi():
    const = float(0)
    for n in range(0, 36):
        const = const + 1 / ((2 * n + 1) * ((-3) ** n))
    return str(2 * (3 ** 0.5) * const)


i = input("Введите нужную точность: ")

print(find_pi()[:len(i)])
