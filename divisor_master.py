# 1) проверка числа на простоту. Все функции модуля принимают на вход натуральные числа от 1 до 1000.

from math import sqrt

def num_simple(n):
    if n <= 1:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input('Input natural number '))
print('1) проверка числа на простоту\n', num_simple(n))

# 2) выводит список всех делителей числа;
def num_divisors(n):
    result = []
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            if n / i == i:
                result.append(i)
            else:
                result.extend([i, n // i])
        i = i + 1
    result.sort()
    return result


print('2) выводит список всех делителей числа\n', num_divisors(n))

# 3) выводит самый большой простой делитель числа.
def num_max_divisor(n):
    if n == 1:
        return None
    return max(list(filter(num_simple, num_divisors(n))))


print('3) выводит самый большой простой делитель числа\n', num_max_divisor(n))

