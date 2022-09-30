'''
3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество
   вхождений одной строки в другой.

   ssabababsdaasd aba -> 2
'''


a = "ababa"
b = "aba"

def f(a, b):
    count = 0
    for i in range(len(a) - len(b)):
        print('->>', a[i:i + len(b)])
        if b == a[i:i + len(b)]:
            count += 1
    return count

