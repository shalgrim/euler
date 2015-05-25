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

if __name__ == '__main__':

    candidates = [1, 2, 3, 4]
    increase_by = 1
    while True:
        candidates = [c+increase_by for c in candidates]
        if candidates[0] % 10000 == 0: print candidates[0] # debugging

        for i, candidate in enumerate(candidates):
            if len(set(PrimeFactorizer.factor_method2(candidate))) >= 4:
                continue
            else:
                increase_by = i + 1
                break

        else:
            print 'answer: {}'.format(candidates[0])
            sys.exit()



