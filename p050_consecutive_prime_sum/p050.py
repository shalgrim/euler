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
from constants import *
from primes.primes import JustInTimePrimes
from primes.PrimeChecker import PrimeChecker

__author__ = 'Scott'

RUN_TO = ONE_MILLION

if __name__ == '__main__':
    pc = PrimeChecker()
    all_primes = JustInTimePrimes(TEN_MILLION)

    start_prime_idx = ZERO
    start_prime = all_primes[start_prime_idx]
    overall_longest_length = ZERO
    next_prime_idx = start_prime_idx + overall_longest_length
    next_prime = all_primes[next_prime_idx]
    initial_sum = ZERO

    while initial_sum < RUN_TO:

        current_longest_list = \
            all_primes[start_prime_idx : next_prime_idx]

        current_sum = sum(current_longest_list)
        next_prime_idx = start_prime_idx + overall_longest_length
        found_longer = False

        while current_sum < RUN_TO:

            if pc.is_prime(current_sum):
                found_longer = True
                current_longest_list = all_primes[start_prime_idx :
                                                  next_prime_idx]

            current_sum += all_primes[next_prime_idx]
            next_prime_idx += 1

        if found_longer:
            overall_longest_length = len(current_longest_list)
            overall_longest_sum = sum(current_longest_list)
            final_prime = current_longest_list[-1]
            print 'found {} element list from {} to {} summing to {}'.format(
                overall_longest_length, start_prime, final_prime,
                overall_longest_sum
            )

        start_prime_idx += 1
        start_prime = all_primes[start_prime_idx]
        next_prime_idx = start_prime_idx + overall_longest_length
        next_prime = all_primes[next_prime_idx]
        initial_sum = sum(all_primes[start_prime_idx : next_prime_idx])
        print start_prime, next_prime, initial_sum

    print 'overall longest sums to {}'.format(overall_longest_sum)
    sys.exit()
    # just me playin' around below here
    num_primes = 0
    for p in prime_generator(ONE_MILLION):
        num_primes += 1
        print p
    print num_primes

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
