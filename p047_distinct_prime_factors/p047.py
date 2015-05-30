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

        if len(set(PrimeFactorizer.factor_method2(candidate))) >= \
                NUM_PRIME_FACTORS:
            consecutive_found += 1
        else:
            consecutive_found = 0

    endtime = datetime.datetime.now()

    print 'answer: {}'.format(candidate + 1 - NUM_PRIME_FACTORS)
    print 'timing: {}'.format(endtime - starttime)

    # took 2:52 with method2
    # took 3:07 with method1
    # So I think next steps are to make sure method1 is working correctly as
    # it should be saving us considerable time
    # alternatively do something where you cache known primes as generating
    # those may be part of the problem
    # so could do some profiling to look at that

    # 5/30/15
    # just checked out this revision (d60a8278) and it takes 3:07 with method 1
    # and 2:52 with method 2 so this is a good place to start over since I'd
    # managed to make everything run slower in my changes after this

    # So let's profile method2 again
    # It says it's spending 165 seconds in _is_prime
    # Let's make my first change changing range to xrange in that method

    # That took it down to 72 seconds
    # And it's still spending 64 seconds of that in _is_prime

    # And then I got it by reworking _is_prime to keep track of a "starting
    # point" of numbers where we don't know whether it's prime or not to
    # start from instead of starting from 2 every time. it runs in 30 seconds





