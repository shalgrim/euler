import sys

class PrimeChecker(object):
    """provides functionality for checking if number is prime also caches known primes"""

    ONE_DIGIT_PRIMES = set([2, 3, 5, 7])

    def __init__(self):
        self._known_primes = set()
        self._known_non_primes = set()
        self._known_primes_sorted = []
        self._highest_n_checked = 1
        self._starting_point = 2

        return

    def get_known_primes(self):
        return self._known_primes

    def get_sorted_known_primes(self):
        return self._known_primes_sorted

    def add_prime(self, p):
        assert isinstance(p, int)
        assert p >= 2
        self._known_primes.add(p)
        self._known_primes_sorted = sorted(self._known_primes) # this should
                                                               # be in primes
                                                               # setter
        return self.get_known_primes()

    def get_highest_n_checked(self):
        return self._highest_n_checked

    def _set_highest_n_checked(self, n):
        assert isinstance(n, int)
        if self.get_highest_n_checked() > n:
            return -1

        self._highest_n_checked = n
    
        return self.get_highest_n_checked()

    # def is_prime(self, n):
    #     assert isinstance(n, int)
    #
    #     if n < 2:
    #         return False
    #
    #     if n in self.get_known_primes():
    #         return True
    #
    #     # at this point I have already checked and it's not a prime
    #     if n < self.get_highest_n_checked():
    #         return False
    #
    #     return self._is_prime(n)
    #
    # def _is_prime(self, n):
    #     """
    #     Assume n >= 2 and n is int
    #     """
    #
    #     halfway_point = n / 2
    #     highest = self.get_highest_n_checked()
    #
    #     # first check all the known primes through highest
    #     for kp in self.get_sorted_known_primes():
    #         if n % kp == 0:
    #             # print >> sys.stderr, 'divisible by known prime {}'.format(kp)
    #             return False
    #
    #     # then check all from highest through halfway_point
    #     for i in xrange(highest + 1, halfway_point + 1):
    #         if self.is_prime(i):
    #             if n % i == 0:
    #                 # print >> sys.stderr, 'divisible by new prime {}'.format(i)
    #                 return False
    #
    #     self._set_highest_n_checked(halfway_point)
    #     assert n not in self._known_primes
    #     self.add_prime(n)
    #     return True

    # going to retry clever way since doing it the way below breaks problem 41
    # NB: the clever way works, but it took way longer for p037 to finish
    # I'm not sure if p041 would still crash if I did it clever way but it
    # almost certainly wouldn't finish in a minute
    # Later: Learned that p041 was crashing because I should have been using
    # xrange and also shouldn't have even been bothering with nine-digit
    # pandigitals
    # so going back to brute force way for p041
    def is_prime(self, n):
        assert isinstance(n, int)

        if n < 2:
            return False

        if n in self.get_known_primes():
            return True

        if n in self._known_non_primes:
            return False

        return self._is_prime(n)

    def unknown_generator(self, n):
        """
        Generates all integers x such that 2 <= x < n and x is not known to
        be prime or non-prime (composite)
        """

        knowns = self.get_known_primes().union(self._known_non_primes)

        for i in range(2, n):
            if i not in knowns:
                yield i

    def _is_prime(self, n):
        """
        Assume n >= 2 and n is int
        """

        if self._is_divisible_by_known_prime(n):
            answer = False

        else:
            for i in xrange(self._starting_point, n):
                if n%i == 0:
                    self._known_non_primes.add(n)
                    answer = False
                    break
            else:
                self.add_prime(n)
                answer = True

        if n == self._starting_point:
            self._starting_point += 1

        return answer

    def _is_divisible_by_known_prime(self, n):
        for p in self.get_sorted_known_primes():
            if n%p == 0:
                self._known_non_primes.add(n)
                return True

        return False

    def is_truncatable_prime(self, n):
        assert isinstance(n, int)
        if n < 23: return False
        digits = str(n)
        if int(digits[0]) not in self.ONE_DIGIT_PRIMES: return False
        if int(digits[-1]) not in self.ONE_DIGIT_PRIMES: return False

        ints_to_check = set([n])

        for i in range(2, len(digits)):
            ints_to_check.add(int(digits[:i])) # first i digits
            ints_to_check.add(int(digits[-i:])) # last i digits

        for itc in ints_to_check:
            if not self.is_prime(itc): return False

        return True
