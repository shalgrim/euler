__author__ = 'Scott'

def prime_generator(n):
    """
    generates primes less than n in order
    :param n: upper limit of possible primes, inclusive
    :return: yields each prime <= n
    """
    known_primes = []
    i = 1
    while i < n:
        i += 1
        primes_to_check = [kp for kp in known_primes if kp <= i/2]
        for prime in primes_to_check:
            if i % prime == 0:
                break
        else:
            known_primes.append(i)
            yield i


class JustInTimePrimes(object):

    def __init__(self, n):
        self.pg = prime_generator(n)
        self.prime_list = []
        return

    def __getitem__(self, a):
        while len(self.prime_list) <= a:
            self.prime_list.append(self.pg.next())

        return self.prime_list[a]

    def __getslice__(self, a, b):
        while len(self.prime_list) <= b:
            try:
                self.prime_list.append(self.pg.next())
            except StopIteration:
                pass

        return self.prime_list[a:b]

