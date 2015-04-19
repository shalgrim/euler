"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

import math, sys
from pandigitals.pandigitals import get_nine_digit_pandigitals

if __name__ == '__main__':
    # algorithm
    # generate all 9-digit pandigitals
    nine_digit_pandigitals = get_nine_digit_pandigitals()
    assert len(nine_digit_pandigitals) == math.factorial(9)

    # order them in reverse
    nine_digit_pandigitals.sort(reverse=True)

    for ndp in nine_digit_pandigitals:
        # you start by taking the first digit and multiply it by two and see

        for first_num_len in range(1, 5):
            building = int(str(ndp)[:first_num_len])
            first_num = int(building)
            multiplier = 1

            while str(building) == str(ndp)[:len(str(building))]:
                if len(str(building)) == 9:
                    print 'answer: {}, factor: {}'.format(ndp, first_num)
                    sys.exit()
                multiplier += 1
                next_num = first_num * multiplier
                concatenated_num = str(building) + str(next_num)
                building = int(concatenated_num)
