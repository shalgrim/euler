"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import math, sys
from pandigitals.pandigitals import get_nine_digit_pandigitals
from primes.PrimeChecker import PrimeChecker

__author__ = 'Scott'

if __name__ == '__main__':
    # generate all 9-digit pandigitals
    nine_digit_pandigitals = get_nine_digit_pandigitals()
    assert len(nine_digit_pandigitals) == math.factorial(9)

    # order them in reverse
    nine_digit_pandigitals.sort(reverse=True)

    pc = PrimeChecker()

    for ndp in nine_digit_pandigitals:
        if pc.is_prime(ndp):
            print 'answer: {}'.format(ndp)
            sys.exit()

    print 'did not find one'

