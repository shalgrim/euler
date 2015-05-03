"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

import sys
from copy import copy
from primes.primes import prime_generator
from primes.PrimeChecker import PrimeChecker

__author__ = 'Scott'

NEGATIVE_ONE = -1
ZERO = 0
ONE = 1
TWO = 2
ONE_HUNDRED = 100
ONE_THOUSAND = 1000
ONE_MILLION = 1000000

# def get_longest_consec_prime_sum_under_n_starting_with_k(n, k):
#     """
#     return longest sum of consecutive primes starting with k that adds to a
#     prime below n
#     :param n: the number our sum must not go over
#     :param k: the first number
#     :return: a list of 0 or more consecutive primes that sum to a prime below n
#     """
#     assert isinstance(n, int)
#     assert isinstance(k, int)
#     assert PrimeChecker.is_prime(k), 'starting number must be prime'
#
#     if k < n:
#         return []
#
#     answer = []
#     longest_list = [k]
#     current_list = [k]
#     current_sum = sum(current_list)
#
#     while sum(current_list) < n:
#         if PRIME_CHECKER.is_prime(current_sum):
#             longest_list = copy(current_list)
#   BAILED OUT WHILE WRITING TO TAKE ANOTHER DIRECTION


if __name__ == '__main__':
    all_primes_list = []
    pc = PrimeChecker()
    pg = prime_generator(ONE_MILLION)

    start_prime_idx = NEGATIVE_ONE
    start_prime = NEGATIVE_ONE
    overall_longest_length = ZERO

    while start_prime < ONE_MILLION:
        start_prime_idx += 1

        try:
            start_prime = all_primes_list[start_prime_idx]
        except IndexError:
            all_primes_list.append(pg.next())
            start_prime = all_primes_list[start_prime_idx]

        current_sum = start_prime
        current_longest_list = [start_prime]
        next_prime_idx = start_prime_idx

        while current_sum < ONE_MILLION:
            next_prime_idx += 1

            try:
                current_sum += all_primes_list[next_prime_idx]
            except IndexError:
                all_primes_list.append(pg.next())
                current_sum += all_primes_list[next_prime_idx]

            if current_sum < ONE_MILLION and pc.is_prime(current_sum):
                current_longest_list = all_primes_list[start_prime_idx :
                                                       next_prime_idx+ONE]

        # invariant: longest_list holds longest list starting at k
        print 'longest list start at {} is {} long and sums to {}'.format(
            start_prime, len(current_longest_list), sum(current_longest_list))
        if len(current_longest_list) > overall_longest_length:
            overall_longest_length = len(current_longest_list)
            overall_longest_sum = sum(current_longest_list)

    print 'overall longest sums to {}'.format(overall_longest_sum)
    sys.exit()
    # just me playin' around below here
    num_primes = 0
    for p in prime_generator(ONE_MILLION):
        num_primes += 1
        print p
    print num_primes

