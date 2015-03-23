"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
"""

__author__ = 'Scott'


def get_numbers_with_shared_digit(seed_num):
    """
    :param seed_num: a two-digit number from which we'll generate all two-digit
    numbers that share at least one digit with x
    :return: answer - a set of all two-digit numbers that share at least one
    digit with seed_num
    """
    assert 10 <= seed_num <= 99, 'Input must be two digits long'

    tens_digit = seed_num / 10
    ones_digit = seed_num % 10

    # TODO: clean this up with DRY
    # TODO: perfect candidate for unit testing
    answer = [tens_digit * 10 + i for i in range(0, 10)]
    answer += [i*10 + tens_digit for i in range(1, 10)]

    if ones_digit > 0:
        answer += [ones_digit * 10 + i for i in range(0, 10)]

    answer += [i*10 + ones_digit for i in range(1, 10)]
    answer = set(answer)

    return answer


def generate_denoms_by_num(nums):
    answer = {}
    raise NotImplementedError

    for num in nums:
        possible_nums = generate_denoms_by_num(num)
        answer[num] = [i for i in range(13, 99)]
    return answer


if __name__ == '__main__':

    # all possible numerators are two-digit numbers not divisible by 11
    nums = [i for i in range(12, 99) if i % 11 != 0]

    # for each numerator, get its possible denominators
    #   mainly meaning two-digit numbers with at least one shared digit
    #   also numerator must be < denominator
    #   also if numerator is divisible by 10, denominator can't be

    denoms_by_num = generate_denoms_by_num(nums)
