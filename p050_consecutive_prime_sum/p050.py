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

from copy import copy
from primes.primes import prime_generator
from primes.PrimeChecker import PrimeChecker

__author__ = 'Scott'

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
    # let's assume two things
    # first, let's assume I have a list of all the primes <= the first prime
    # number greater than 500,000
    all_primes_list = []

    # second, let's assume I'm only trying to find the longest consecutive
    # list starting from some known prime. let's say the index of that prime
    # is k
    k = 2 # for now
    i = k
    current_sum = all_primes_list[k]
    longest_list = all_primes_list[k:i+1]
    pc = PrimeChecker()

    while current_sum < ONE_MILLION:
        i += 1
        current_sum += all_primes_list[i]
        if pc.is_prime(current_sum):
            longest_list = all_primes_list[k:i+1]

    # invariant: longest_list holds longest list starting at k
    # next: figure out how to integrate the generator and start from
    # different k's


    # just me playin' around below here
    num_primes = 0
    for p in prime_generator(ONE_MILLION):
        num_primes += 1
        print p
    print num_primes

