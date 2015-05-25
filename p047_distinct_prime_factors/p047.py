"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
"""

from primes.prime_factorizer import PrimeFactorizer
import sys

__author__ = 'Scott'

NUM_PRIME_FACTORS = 4

if __name__ == '__main__':

    candidate = 1
    consecutive_found = 0

    while consecutive_found < NUM_PRIME_FACTORS:
        candidate += 1

        if candidate % 10000 == 0:
            print candidate # debugging

        if len(set(PrimeFactorizer.factor_method2(candidate))) >= \
                NUM_PRIME_FACTORS:
            consecutive_found += 1
        else:
            consecutive_found = 0

    print 'answer: {}'.format(candidate + 1 - NUM_PRIME_FACTORS)





