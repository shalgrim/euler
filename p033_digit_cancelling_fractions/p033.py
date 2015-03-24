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


def get_two_digit_nums_from_single_digit(single_digit):
    """
    Produce a list of all two-digit numbers that have at least one digit
    equal to single_digit
    :param single_digit: a digit between 0 and 9 inclusive
    :return: answer - list of all two-digit numbers that have single_digit in them
    """
    assert isinstance(single_digit, int)
    assert 0 <= single_digit <= 9
    answer = {i*10 + single_digit for i in range(1, 10)}

    if single_digit > 0:
        answer.update({single_digit * 10 + i for i in range(0, 10)})

    return answer

def get_numbers_with_shared_digit(seed_num):
    """
    :param seed_num: a two-digit number from which we'll generate all two-digit
    numbers that share at least one digit with x
    :return: answer - a set of all two-digit numbers that share at least one
    digit with seed_num
    """
    assert isinstance(seed_num, int)
    assert 10 <= seed_num <= 99, 'Input must be two digits long; input: ' \
                                                        '{}'.format(seed_num)

    tens_digit = seed_num / 10
    ones_digit = seed_num % 10

    answer = get_two_digit_nums_from_single_digit(tens_digit)
    answer.update(get_two_digit_nums_from_single_digit(ones_digit))

    answer = set(answer)

    return answer


def generate_denoms_for_num(numerator):
    """
    generate the possible denominators for each numerator
    :param numerator: a two-digit number
    :return: answer - all possible denominators for that numerator in this
    problem
    """

    # get all two-digit numbers with a shared digit
    possibles = get_numbers_with_shared_digit(numerator)
    assert isinstance(possibles, set)

    # then reduce to only those > num
    possibles = [denom for denom in possibles if denom > numerator]
    assert isinstance(possibles, list)

    return answer

def generate_denoms_for_nums(nums):
    """
    generate the possible denominators for each numerator
    :param nums: a list of the possible numerators
    :return: answer - a dict whose keys are numerators and whose values are
    lists of the possible denominators
    """
    answer = {}
    # TODO: create tests
    raise NotImplementedError

    for num in nums:
        answer[num] = generate_denoms_for_num(num)

    return answer


if __name__ == '__main__':

    # all possible numerators are two-digit numbers not divisible by 11
    nums = [i for i in range(12, 99) if i % 11 != 0]

    # for each numerator, get its possible denominators
    #   mainly meaning two-digit numbers with at least one shared digit
    #   also numerator must be < denominator
    #   also if numerator is divisible by 10, denominator can't be

    denoms_by_num = generate_denoms_by_num(nums)
