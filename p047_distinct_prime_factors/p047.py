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
from project_euler.primes.prime_factorizer import PrimeFactorizer

__author__ = 'Scott'

NUM_PRIME_FACTORS = 4

if __name__ == '__main__':

    starttime = datetime.datetime.now()

    candidate = 1
    consecutive_found = 0

    while consecutive_found < NUM_PRIME_FACTORS:
        candidate += 1
        if candidate % 10000 == 0:
            print candidate, datetime.datetime.now() - starttime # debugging

        if len(set(PrimeFactorizer.factor_method2(candidate))) >= \
                NUM_PRIME_FACTORS:
            consecutive_found += 1
        else:
            consecutive_found = 0

    endtime = datetime.datetime.now()

    print 'answer: {}'.format(candidate + 1 - NUM_PRIME_FACTORS)
    print 'timing: {}'.format(endtime - starttime)

    # took 2:52 with method2
    # took 3:44 with method1, was only 3:07 before I "fixed" it
    # I fixed it again and now it took 3:22 just to get to n = 10000

    # Then I added method 3 and that takes 10 times longer (NUM_PRIME_FACTORS
    #  = 3) then method 2, which is amazeballs

    # ... maybe do profiling now
    # alternatively do something where you cache known primes as generating
    # those may be part of the problem
    # so could do some profiling to look at that

    # I did some profiling and the single biggest time suck is
    # PrimeChecker._is_prime at 85 seconds

    # Ima profile method 2, which the last time took 3:20, but I had
    # debugging prints in there
    # results of that are that I spent almost all of my time, over three
    # minutes, in _is_prime

    # Well I tried to fix that and now that's taking forever (not sure it's
    # ever going to finish)
    # I think the problem is going to be in prime generator generating the
    # same primes over and over again
    # So the solution is going to be to cache known primes higher up in the
    # solution





