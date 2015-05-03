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

if __name__ == '__main__':
    # not super clear but Ima assume that the indexes are supposed to always
    # be the same
    # So solution is to generate all 0-9 pandigitals and then see if they fit
    # NB that I think we ignore those that start with 0
    # Actually I think a good way to do this is to keep track of
    # possibilities by first generating all possible four-digit numbers (
    # e.g., even ones), then from those generate possible five-digit prefixes
    #  by only adding digits that get you divisible by three and so on
    raise NotImplementedError
