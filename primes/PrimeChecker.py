from project_euler.primes.primes import prime_generator

class PrimeChecker(object):
    """provides functionality for checking if number is prime also caches known primes"""

    ONE_DIGIT_PRIMES = set([2, 3, 5, 7])
    _known_primes = set()
    _known_non_primes = set()
    _known_primes_sorted = []
    _highest_n_checked = 1

    @classmethod
    def get_known_primes(cls):
        return cls._known_primes

    @classmethod
    def get_sorted_known_primes(cls):
        return cls._known_primes_sorted

    @classmethod
    def add_prime(cls, p):
        assert isinstance(p, int)
        assert p >= 2
        cls._known_primes.add(p)
        cls._known_primes_sorted = sorted(cls._known_primes)
        return cls.get_known_primes()

    @classmethod
    def get_highest_n_checked(cls):
        return cls._highest_n_checked

    @classmethod
    def _set_highest_n_checked(cls, n):
        assert isinstance(n, int)
        if cls.get_highest_n_checked() > n:
            return -1

        cls._highest_n_checked = n
    
        return cls.get_highest_n_checked()

    @classmethod
    def is_prime(cls, n):
        assert isinstance(n, int)

        if n < 2:
            return False

        if n in cls.get_known_primes():
            return True

        if n in cls._known_non_primes:
            return False

        return cls._is_prime(n)

    @classmethod
    def _is_prime(cls, n):
        """
        Assume n >= 2 and n is int
        """
        for prime in prime_generator(n-1):
            if n % prime == 0:
                cls._known_non_primes.add(n)
                return False

        cls.add_prime(n)
        return True

    @classmethod
    def is_truncatable_prime(cls, n):
        assert isinstance(n, int)
        if n < 23: return False
        digits = str(n)
        if int(digits[0]) not in cls.ONE_DIGIT_PRIMES: return False
        if int(digits[-1]) not in cls.ONE_DIGIT_PRIMES: return False

        ints_to_check = set([n])

        for i in range(2, len(digits)):
            ints_to_check.add(int(digits[:i])) # first i digits
            ints_to_check.add(int(digits[-i:])) # last i digits

        for itc in ints_to_check:
            if not cls.is_prime(itc): return False

        return True
