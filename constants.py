import math

__author__ = 'Scott'

# ints
NEGATIVE_ONE = -1
ZERO = 0
ONE = 1
TWO = 2
ONE_HUNDRED = 100
ONE_THOUSAND = 1000
TEN_THOUSAND = 10000
ONE_MILLION = 1000000
TEN_MILLION = 10000000

try:
    INFINITY = math.isinf         # python 3
except AttributeError:
    INFINITY = float("infinity")  # python 2

# string
MAIN_PROCESS = '__main__'
