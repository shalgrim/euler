__author__ = 'Scott'

from PrimeChecker import PrimeChecker

class PrimeFactorizer(object):
    """
    generates the prime factorization of an integer
    """

    pc = PrimeChecker()
    known_factorizations = {}

    @classmethod
    def factor(cls, n):
        assert isinstance(n, int), 'factorize only accepts int input'
        if n in PrimeFactorizer.known_factorizations:
            return PrimeFactorizer.known_factorizations[n]

        factors = []
        reduced = n

        while not cls.pc.is_prime(reduced):
            sp = cls._find_smallest_prime(reduced)
            factors.append(sp)
            reduced /= sp

        factors.append(reduced)
        factors.sort()
        PrimeFactorizer.known_factorizations[n] = factors
        return factors


    @classmethod
    def _find_smallest_prime(cls, n):
        assert isinstance(n, int)

        if cls.pc.is_prime(n):
            return n




