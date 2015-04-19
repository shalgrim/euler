from itertools import permutations

__author__ = 'Scott'


def get_nine_digit_pandigitals():
    """
    originally written for p038
    :return: all nine-digita pandigitals
    """
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = [int(''.join(p)) for p in permutations(digits)]

    return answer