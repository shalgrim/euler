"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

__author__ = 'Scott'

# So I'm trying to find three four-digit numbers
# And here are my constraints
# 1) All three are prime
# 2) All three are permutations of each other
# 3) The three numbers make an arithmetic sequence, which means they increase by
#    a set amount

# Brute Force Approach:
# For each prime 1000 <= x <= 9999
#   generate its permutations
#   if it has at least two other unique permutations
#       if it has at least two other unique prime permutations
#           Can you generate a sequence out of those three numbers?

# So the first thing I want to do is write a find_arithmetic_sequence(nums, n)
# method which will return all possible arithmetic sequences of length n from
# the set(?) of numbers in nums
