"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
__author__ = 'Scott'

from itertools import combinations, permutations
from constants import ZERO, TWO

DIGITS = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

def gen_divis_by_2():
    final_digits = {d for d in DIGITS if d % TWO == ZERO}

    for fd in final_digits:
        remaining_digits = DIGITS.difference(set([fd]))

        for combo in combinations(remaining_digits, 2):
            for permute in permutations(combo):
                yield (permute[0], permute[1], fd)


def gen_divis_by(divis_by, *taken_digits):
    remaining_digits = DIGITS.difference(set(*taken_digits))

    for rd in remaining_digits:
        
        if int('{}{}{}'.format(taken_digits[-2], taken_digits[-1], rd)) % \
                divis_by == 0:
            yield rd


def gen_divis_by_3(d2, d3, d4):
    remaining_digits = DIGITS.difference({d2, d3, d4})

    for rd in remaining_digits:
        if int('{}{}{}'.format(d3, d4, rd)) % 3 == 0:
            yield rd


def gen_divis_by_5(d2, d3, d4, d5):
    remaining_digits = DIGITS.difference({d2, d3, d4, d5})

    for rd in remaining_digits:
        if int('{}{}{}'.format(d4, d5, rd)) % 5 == 0:
            yield rd

def gen_divis_by_7(d2, d3, d4, d5, d6):
    remaining_digits = DIGITS.difference({d2, d3, d4, d5, d6})

    for rd in remaining_digits:
        if int('{}{}{}'.format(d5, d6, rd)) % 7 == 0:
            yield rd

def gen_divis_by_11(d2, d3, d4, d5, d6, d7):
    remaining_digits = DIGITS.difference({d2, d3, d4, d5, d6, d7})

    for rd in remaining_digits:
        if int('{}{}{}'.format(d6, d7, rd)) % 11 == 0:
            yield rd

def gen_divis_by_13(d2, d3, d4, d5, d6, d7, d8):
    remaining_digits = DIGITS.difference({d2, d3, d4, d5, d6, d7, d8})

    for rd in remaining_digits:
        if int('{}{}{}'.format(d7, d8, rd)) % 13 == 0:
            yield rd

def gen_divis_by_17(d2, d3, d4, d5, d6, d7, d8, d9):
    remaining_digits = DIGITS.difference({d2, d3, d4, d5, d6, d7, d8, d9})

    for rd in remaining_digits:
        if int('{}{}{}'.format(d8, d9, rd)) % 17 == 0:
            yield rd

if __name__ == '__main__':
    # not super clear but Ima assume that the subscripts are supposed to always
    # be the same
    # So solution is to generate all 0-9 pandigitals and then see if they fit
    # NB that I think we ignore those that start with 0
    # Actually I think a good way to do this is to keep track of
    # possibilities by first generating all possible four-digit numbers (
    # e.g., even ones), then from those generate possible five-digit prefixes
    #  by only adding digits that get you divisible by three and so on

    # so let's break this up
    # part 1: generate all possible d2d3d4 divisible by 2
    # NB: based on the example for d3d4d5 Ima assume that d2 can be 0

    special_pandigitals = []

    for d2, d3, d4 in gen_divis_by_2():
        for d5 in gen_divis_by_3(d2, d3, d4):
            for d6 in gen_divis_by_5(d2, d3, d4, d5):
                for d7 in gen_divis_by_7(d2, d3, d4, d5, d6):
                    for d8 in gen_divis_by_11(d2, d3, d4, d5, d6, d7):
                        for d9 in gen_divis_by_13(d2, d3, d4, d5, d6, d7, d8):
                            for d10 in gen_divis_by_17(d2, d3, d4, d5, d6,
                                                       d7, d8, d9):
                                d1 = list(DIGITS.difference({d2, d3, d4, d5, d6,
                                                        d7, d8, d9, d10}))[0]

                                if d1 > 0:
                                    spec_pd = int('{}{}{}{}{}{}{}{}{}{}'.format(
                                        d1, d2, d3, d4, d5, d6, d7, d8, d9,
                                        d10))
                                    special_pandigitals.append(spec_pd)

    print 'answer: {}'.format(sum(special_pandigitals))
