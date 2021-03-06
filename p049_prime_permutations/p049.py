"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from itertools import permutations, combinations
from constants import ONE, MAIN_PROCESS, ONE_THOUSAND, TEN_THOUSAND
from primes.primes import prime_generator
from primes.PrimeChecker import PrimeChecker

__author__ = 'Scott'


def find_first_arithmetic_sequence(numset, n=3):
    """

    :param numset: a set of numbers
    :param n: desired length of arithmetic sequence
    :return: first identified arithmetic sequence of length n from numset, None
        if none found
    """

    # input assertions
    assert isinstance(numset, set)
    assert isinstance(n, int)

    sorted_nums = sorted(list(numset))

    for num in sorted_nums:
        assert isinstance(num, int)

    # check impossible-to-find case
    if len(sorted_nums) < n:
        return None

    # check trivial case
    if len(sorted_nums) == n:
        if is_arithmetic_sequence(sorted_nums):
            return sorted_nums
        else:
            return None

    # case where numset is longer than n
    assert len(sorted_nums) > n

    # last_start_ind is the last potential starting index for a sequence of
    # length n
    last_start_ind = len(sorted_nums) - n

    sorted_nums = sorted(list(numset))

    # check all possible sequences for being arithmetic sequence
    for start_ind in range(last_start_ind + ONE):
        potential_sequence = sorted_nums[start_ind : start_ind + n]

        if is_arithmetic_sequence(potential_sequence):
            return potential_sequence

    # could not find arithmetic sequence
    return None

# There should also be one method that just detects whether or not the
# numbers provided do form an arithmetic sequence

def is_arithmetic_sequence(nums):
    """
    determines if nums, when sorted, is an arithmetic sequence.
    if len(nums) == 0: returns False
    if 0 < len(nums) <= 2: returns True
    :param nums: list of ints
    :return: True if nums, when sorted, is an arithmetic sequence
    """
    assert isinstance(nums, list)

    # assert each element in nums is an int
    assert all([isinstance(n, int) for n in nums])

    if len(nums) > 2:
        # sort them and get the differences as a list
        nums.sort()
        diffs = [nums[i+1] - n for i, n in enumerate(nums[:-1])]

        # verify all the diffs are equal
        answer = all([diffs[i+1] == d for i, d in enumerate(diffs[:-1])])
    elif len(nums) > 0:
        answer = True
    else:   # len(nums) == 0
        answer = False

    return answer


def int_permutes(n):
    """
    wraps itertools.permutations in creating permutations of the digits of
    an int
    :param n: an int
    :return: generator of the permutations of n
    """
    assert isinstance(n, int)
    nstr = str(n)
    digit_list = [c for c in nstr]

    wrapped_generator = permutations(digit_list)

    for digit_tuple in wrapped_generator:
        yield int(''.join(digit_tuple))

    raise StopIteration

if __name__ == MAIN_PROCESS:


    # So I'm trying to find three four-digit numbers
    # And here are my constraints
    # 1) All three are prime
    # 2) All three are permutations of each other
    # 3) The three numbers make an arithmetic sequence, which means they increase by
    #    a set amount

    # Brute Force Approach:
    # For each prime 1000 <= x <= 9999

    prime_gen = prime_generator(TEN_THOUSAND)
    prime_checker = PrimeChecker()

    for prime in prime_gen:
        if prime < 1000:
            continue

        # get its list of prime permutations greater than 1000
        unique_permutes = set([int(p) for p in int_permutes(prime) if
                               int(p) >= 1000])
        unique_prime_permutes = {up for up in unique_permutes if
                                 prime_checker.is_prime(up)}

        if len(unique_prime_permutes) >= 3:
            for combo in combinations(unique_prime_permutes, 3):
                answer = find_first_arithmetic_sequence(set(combo), 3)
                if answer:
                    print ''.join([str(a) for a in answer])
