__author__ = 'Scott'


from PrimeChecker import PrimeChecker

def prime_generator(n):
    """
    generates primes less than n in order
    :param n: upper limit of possible primes, non-inclusive
    :return: yields each prime < n
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

# def prime_generator_from(n, k):
#     """
#     generates primes less than n in order starting with k
#     :param n: upper limit of possible primes, non-inclusive
#     :param k: first prime returned
#     :return: yields each prime from k through n non-inclusive
#     """
#     known_primes = []
#     pc = PrimeChecker()
#     assert isinstance(n, int)
#     assert isinstance(k, int)
#     assert k < n
#     assert pc.is_prime(k)
#     i = k
#     while i < n:
#   BAILED OUT WHILE WRITING TO PURSUE ANOTHER DIRECTION

