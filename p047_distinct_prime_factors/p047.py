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
    while True:
        candidates = [c+1 for c in candidates]
        if candidates[0] % 10000 == 0: print candidates[0] # debugging

        for candidate in candidates:
            if len(set(PrimeFactorizer.factor(candidate))) >= 4:
                continue
            else:
                break

        else:
            print 'answer: {}'.format(candidates[0])
            sys.exit()



