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


def generate_numerators():
    answer = [i for i in range(12, 99) if i % 11 != 0]

    return answer


def generate_two_digit_numbers_with_shared_digit(x):
    assert 10 <= x <= 98

    tens_digit = x / 10
    ones_digit = x % 10

    # TODO: clean this up with DRY
    # TODO: perfect candidate for unit testing
    answer = [tens_digit * 10 + i for i in range(0, 10)]
    answer += [i*10 + tens_digit for i in range(1, 10)]
    answer += [ones_digit * 10 + i for i in range(0, 10)]
    answer += [i*10 + ones_digit for i in range(1, 10)]
    answer = set(answer)

    return answer


def generate_denoms_by_num(nums):
    answer = {}
    raise NotImplementedError

    for num in nums:
        answer[num] = [i for i in range(13, 99)]
    return answer

if __name__ == '__main__':
    nums = generate_numerators()
    denoms_by_num = generate_denoms_by_num(nums)
