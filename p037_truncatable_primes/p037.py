"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import itertools, sys
from project_euler.primes.PrimeChecker import PrimeChecker

def generate_truncatable_prime_candidates():
    """
    Generator to build possible candidates for truncatable primes based on
    what digits can possibly go where
    :return:
    """
    anywhere_digits = ['3', '7']      # digits that can go anywhere in candidate
    middle_only_digits = ['1', '9']   # digits that cannot be on either end in
                                      # candidate because can't stand alone
    front_only_digits = ['2']         # digits that can only be the first in
                                      # candidate
    front_or_middle_digits = ['5']    # digits that must not be at end in
                                      # candidate

    can_be_first_digits = anywhere_digits + front_or_middle_digits + front_only_digits
    can_be_middle_digits = anywhere_digits + front_or_middle_digits + middle_only_digits
    can_be_final_digits = anywhere_digits

    candidate_length = 2

    while True:

        # debug statement
        if candidate_length % 100 == 0:
            print >> sys.stderr, 'candidate_length: {}'.format(candidate_length)

        # first step, generate first number
        for first_digit in can_be_first_digits:

            # second step, generate last number
            for final_digit in can_be_final_digits:

                # finally, generate all permutations of middle digits
                # have to do combinations_with_replacement first to get
                # repeated elements

                if first_digit == '7' and final_digit == '7' and \
                        candidate_length == 6:
                    pass
                for middle_digit_combo in \
                        itertools.combinations_with_replacement(
                                can_be_middle_digits, candidate_length - 2):
                    for middle_digits in itertools.permutations(middle_digit_combo, candidate_length - 2):
                        middle_string = ''.join(middle_digits)
                        candidate_string = first_digit + middle_string + final_digit
                        assert len(candidate_string) == candidate_length
                        candidate_int = int(candidate_string)
                        yield candidate_int

        candidate_length += 1

if __name__ == '__main__':

    truncatable_primes = set()
    prime_checker = PrimeChecker()

    # # ATTEMPT #1 BRUTE FORCE
    # # It got me 10 truncatable primes then took forever to find next
    #
    # num = 10
    # while len(truncatable_primes) < 11:
    #     if num % 10000 == 0: print num
    #     if prime_checker.is_truncatable_prime(num):
    #         print 'adding truncatable prime: {}'.format(num)
    #         truncatable_primes.add(num)
    #     num += 1

    # ATTEMPT #2
    # Trying to generate candidates based on what possible digits can go where

    candidate_length = 1
    for candidate in generate_truncatable_prime_candidates():
        if len(str(candidate)) > candidate_length:
            candidate_length = len(str(candidate))
            print 'new candidate length {}'.format(candidate_length)

        if candidate == 739397: print 'checking 739397'
        if prime_checker.is_truncatable_prime(candidate):
            print 'adding truncatable prime: {}'.format(candidate)
            truncatable_primes.add(candidate)
            if len(truncatable_primes) >= 11:
                break

    print 'answer: {}'.format(sum(truncatable_primes))
