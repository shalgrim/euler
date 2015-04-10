"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from primes.PrimeChecker import PrimeChecker

if __name__ == '__main__':
    truncatable_primes = set()
    prime_checker = PrimeChecker()

    num = 10
    while len(truncatable_primes) < 11:
        if num % 100000 == 0: print num
        if prime_checker.is_truncatable_prime(num):
            print 'adding truncatable prime: {}'.format(num)
            truncatable_primes.add(num)
        num += 1

    print 'answer: {}'.format(sum(truncatable_primes))
