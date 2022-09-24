
'''
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''


def conjunctio(a, b):  # a ⋀ b
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1:
        return 0
    if a == 1 and b == 0:
        return 0
    if a == 1 and b == 1:
        return 1


def disjunctio(a, b):  # a ⋁ b
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1:
        return 1
    if a == 1 and b == 0:
        return 1
    if a == 1 and b == 1:
        return 1


def inversio(a):    # ¬ a
    if a == 1:
        return 0
    if a == 0:
        return 1


def verification_of_approval(x, y, z):  # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
    left_value = inversio(disjunctio(disjunctio(x, y), z))
    right_value = conjunctio(conjunctio(inversio(x), inversio(y)), inversio(z))
    if left_value == right_value:
        return left_value
    else:
        return None


def verification_of_approval_all_value(x, y, z):
    i = 0
    while i < 8:
        print(f"¬({x[i]} ⋁ {y[i]} ⋁ {z[i]}) = {verification_of_approval(x[i], y[i], z[i])} and ",
              f"¬{x[i]} ⋀ ¬{y[i]} ⋀ ¬{z[i]} = {verification_of_approval(x[i], y[i], z[i])}")
        i += 1


x = [0, 1, 0, 1, 0, 1, 0, 1]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]

verification_of_approval_all_value(x, y, z)
