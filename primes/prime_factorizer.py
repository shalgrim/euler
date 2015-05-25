__author__ = 'Scott'

from primes import prime_generator
from PrimeChecker import PrimeChecker

class PrimeFactorizer(object):
    """
    generates the prime factorization of an integer
    """

    pc = PrimeChecker()
    known_factorizations = {}

    @classmethod
    def factor_method1(cls, n):
        answer = cls._factor(n, [])

        return answer


    @classmethod
    def factor_method2(cls, n):
        factors = []
        reduced = n

        while not cls.pc.is_prime(reduced):
            sp = cls._find_smallest_prime(reduced)
            factors.append(sp)
            reduced /= sp

        factors.append(reduced)
        factors.sort()
        return factors

    @classmethod
    def _factor(cls, n, factors):
        assert isinstance(n, int)
        assert isinstance(factors, list)

        if n in PrimeFactorizer.known_factorizations:
            return factors + PrimeFactorizer.known_factorizations[n]

        if cls.pc.is_prime(n):
            cls.known_factorizations[n] = [n]
            factors.append(n)
            return factors

        smallest_prime = cls._find_smallest_prime(n)
        factors.append(smallest_prime)
        reduced = n / smallest_prime
        return cls._factor(reduced, factors)


    @classmethod
    def _find_smallest_prime(cls, n):
        assert isinstance(n, int)

        if cls.pc.is_prime(n):
            return n

        pg = prime_generator(n)

        for prime in pg:
            if n % prime == 0:
                return prime

        raise Exception, 'no smallest prime found'
