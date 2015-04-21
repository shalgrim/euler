"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import math, sys
from pandigitals.pandigitals import get_seven_digit_pandigitals
from primes.PrimeChecker import PrimeChecker

__author__ = 'Scott'

if __name__ == '__main__':
    # generate all 9-digit pandigitals
    # I can skip 9-digit pandigitals b/c they're always divisible by 3
    # because their digits always add up to 10 * 4 + 5 = 45
    # nine_digit_pandigitals = get_nine_digit_pandigitals()
    # assert len(nine_digit_pandigitals) == math.factorial(9)

    # 8-digit pandigitals always add up to 9*4 = 36 so also divisible by 3

    # 7-digit pandigitals always add up to 8 * 3 + 4 = 28 so I can start here
    # generate all 7-digit pandigitals
    seven_digit_pandigitals = get_seven_digit_pandigitals()
    assert len(seven_digit_pandigitals) == math.factorial(7)

    # order them in reverse
    seven_digit_pandigitals.sort(reverse=True)

    pc = PrimeChecker()

    for i, sdp in enumerate(seven_digit_pandigitals):
        if i % 1000 == 0:
            pass            # for debugging
        if pc.is_prime(sdp):
            print 'answer: {}'.format(sdp)
            sys.exit()

    print 'did not find one'

