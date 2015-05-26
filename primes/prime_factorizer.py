__author__ = 'Scott'

from primes import prime_generator
from PrimeChecker import PrimeChecker


class PrimeFactorizer(object):
    """
    generates the prime factorization of an integer
    """

    pc = PrimeChecker()
    known_factorizations = {1: []}  # initialize to base case

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
    def factor_method3(cls, n):
        """
        identical to method2 except checks for reduced to be 1 instead of prime
        and then doesn't add 1 to the factors, natch
        :param n: int we want prime factorization for
        :return: prime factorization
        """
        factors = []
        reduced = n
        while reduced > 1:
            sp = cls._find_smallest_prime(reduced)
            factors.append(sp)
            reduced /= sp

        factors.sort()
        return factors

    @classmethod
    def _factor(cls, n, factors):
        assert isinstance(n, int)
        assert isinstance(factors, list)

        if n in PrimeFactorizer.known_factorizations:
            answer = factors + cls.known_factorizations[n]
            # cls.known_factorizations[n] = answer
            return answer

        # if cls.pc.is_prime(n):
        # cls.known_factorizations[n] = [n]
        #     factors.append(n)
        #     return factors

        smallest_prime = cls._find_smallest_prime(n)
        factors.append(smallest_prime)
        reduced = n / smallest_prime
        answer = cls._factor(reduced, factors)
        cls.known_factorizations[n] = answer
        return answer


    @classmethod
    def _find_smallest_prime(cls, n):
        assert isinstance(n, int)

        pg = prime_generator(n)

        for prime in pg:
            if n % prime == 0:
                return prime

        raise Exception, 'no prime found for {}'.format(n)
