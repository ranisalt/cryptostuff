import math
import random

rnd = random.randrange


class Field:
    def __init__(self, p):
        def order(n):
            i = 1
            while pow(n, i, p) != 1:
                i += i
            return i

        self.limit = p
        self.elements = (x for x in range(p) if p % x != 0)
        self.order = (order(x) for x in self.elements)


def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = ext_gcd(b, a % b)
    return d, y, x - (a // b) * y


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    


def poly_sum(a, b):
    return a + b


def poly_mul(a, b):
    def c(k):
        acc = 0
        for i in range(k + 1):
            acc += (a >> i & 1) * (b >> (k - i) & 1)
        return acc

    result = 0
    for i in range(a.bit_length() + b.bit_length() + 1):
        result += c(i) << i
    return result


def poly_mod(dividend, divider):
    dividend_bl, divider_bl = dividend.bit_length(), divider.bit_length()


def primes(upto):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in primes:
        if prime <= upto:
            yield prime
        else:
            raise StopIteration()

    for i in range(31, upto + 1, 2):
        for a in random.sample(primes, 10):
            if pow(a, i - 1, i) != 1:
                break
        else:
            yield i


def pollard(n, bound=None):
    if bound is None:
        bound = int(n ** .5)

    def factorial(start, stop):
        fact = 1
        val = 1
        for _ in range(1, start):
            fact *= val
            val += 1

        while val < stop:
            fact *= val
            yield fact
            val += 1

    for f in factorial(2, bound):
        remainder = gcd(pow(2, f, n) - 1, n)

        if 1 < remainder < n:
            return gcd(pow(2, f) - 1, n)

    return 1


#x = pollard(618240007109027021)
