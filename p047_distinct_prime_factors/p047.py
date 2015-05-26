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

import datetime
from primes.prime_factorizer import PrimeFactorizer

__author__ = 'Scott'

NUM_PRIME_FACTORS = 4

if __name__ == '__main__':

    starttime = datetime.datetime.now()

    candidate = 1
    consecutive_found = 0

    while consecutive_found < NUM_PRIME_FACTORS:
        candidate += 1

        if len(set(PrimeFactorizer.factor_method1(candidate))) >= \
                NUM_PRIME_FACTORS:
            consecutive_found += 1
        else:
            consecutive_found = 0

    endtime = datetime.datetime.now()

    print 'answer: {}'.format(candidate + 1 - NUM_PRIME_FACTORS)
    print 'timing: {}'.format(endtime - starttime)

    # took 2:52 with method2
    # took 3:44 with method1, was only 3:07 before I "fixed" it

    # ... maybe do profiling now
    # alternatively do something where you cache known primes as generating
    # those may be part of the problem
    # so could do some profiling to look at that





