"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2 x 1^2
15 = 7 + 2 x 2^2
21 = 3 + 2 x 3^2
25 = 7 + 2 x 3^2
27 = 19 + 2 x 2^2
33 = 31 + 2 x 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""

import math
from constants import *
from primes.primes import prime_generator
from primes.PrimeChecker import PrimeChecker

# composite number means non-prime > 1
# i.e., 4, 6, 8, 9, 10, 12, 14, 15, 16, ...
# therefore odd composites are 9, 15, 21, 25, 27, 33, 35, ...

__author__ = 'Scott'

pc = PrimeChecker()

def fits_conjecture(n):
    """
    :param n: an odd composite number
    :return: True if n can be written as a prime plus twice a square. False
    otherwise
    """
    assert isinstance(n, int)
    assert n % TWO == ONE
    assert not pc.is_prime(n)

    pg = prime_generator(n)

    for prime in pg:
        for base in range(1, int(math.sqrt(n))):
            checksum = prime + TWO * (base ** TWO)
            if checksum == n:
                return True

    return False


if __name__ == '__main__':
    pc = PrimeChecker()

    # outline it
    number = 9
    while fits_conjecture(number):
        # print '{} fits conjecture'.format(number)
        number += TWO

        while pc.is_prime(number):
            number += TWO

    print 'answer: {}'.format(number)


