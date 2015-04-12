__author__ = 'Scott'

class Fraction:
    def __init__(self, num, denom):
        self._num = 0
        self._denom = 1
        self.set_numerator(num)
        self.set_denominator(denom)

        return

    def get_numerator(self):
        return self._num

    def get_denominator(self):
        return self._denom

    def set_numerator(self, num):
        assert isinstance(num, int), 'numerator must be int'
        self._num = num

        return self._num

    def set_denominator(self, denom):
        assert isinstance(denom, int) and denom != 0, 'denominator must be ' \
                                                      'non-zero int'
        self._denom = denom

        return self._denom

    def get_reduced(self):
        """
        :return: answer - a new Fraction fully reduced
        """
        # NEXT Write this method
        # so what I need to do here is find the GCD, greatest common divisor,
        #  right?
        gcd = self.get_gcd()
        answer = Fraction(self._num / gcd, self._denom / gcd)
        return answer

    def get_gcd(self):
        """
        :return: the GCD of the numerator and denominator
        """
        # TODO: Does Python have a built-in gcd algorithm?
        if self._num < self._denom:
            lower = self._num
        else:
            lower = self._denom

        gcd = 1
        for i in range(2, lower + 1):
            if self._num % i == 0 and self._denom % i == 0:
                gcd = i

        return gcd


    def remove_digit_from_int(self, number, digit):
        """
        returns integer representing number with digit removed
        :param number: int
        :param digit: char
        :return: answer - int that is number with digit removed
        """
        # TODO: make test cases
        # TODO: make static or non-class function
        number_char_list = list(str(number))
        number_char_list.remove(digit)
        answer = int(''.join(number_char_list))

        return answer

    def generate_cancelled_fractions(self):
        """
        Generates all fractions created by "cancelling" out digit common in
        numerator and denominator
        :return: answer - sorted list of Fractions that are created by
        cancelling out digits common in numerator and denominator
        """
        common_digits = self.get_common_digits()
        answer = []

        for cd in common_digits:
            new_num = self.remove_digit_from_int(self._num, cd)
            new_denom = self.remove_digit_from_int(self._denom, cd)
            assert 0 <= new_num < 10
            assert 1 <= new_denom < 10, 'new_denom {} in Fraction {}'.format(
                new_denom, self)
            answer.append(Fraction(new_num, new_denom))

        answer.sort()

        return answer

    def get_common_digits(self):
        """
        gets digits that are common in numerator and denominator
        :return: a set of the digits, as characters, that are common in numerator
        and denominator
        """
        numerator_digits = set(str(self._num))
        denom_digits = set(str(self._denom))
        answer = numerator_digits.intersection(denom_digits)
        return answer


    def __eq__(self, other):
        """
        :param other: another Fraction
        :return: True if fractions' numerators and denominators are the same,
        otherwise False
        """
        assert isinstance(other, Fraction), 'must only compare Fractions'
        return self.get_numerator() == other.get_numerator() and \
               self.get_denominator() == other.get_denominator()

    def __str__(self):
        return '{}/{}'.format(self.get_numerator(), self.get_denominator())

    def __cmp__(self, other):
        """
        sorts on denominator then on numerator
        :return: -1 if self < other, 0 if equal, 1 if self > other
        """
        assert isinstance(other, Fraction), 'must compare only Fractions'
        if self.get_denominator() != other.get_denominator():
            return cmp(self.get_denominator(), other.get_denominator())
        else:
            return cmp(self.get_numerator(), other.get_numerator())

    def __mul__(self, other):
        assert isinstance(other, Fraction), 'must only multiply Fractions'
        new_num = self.get_numerator() * other.get_numerator()
        new_denom = self.get_denominator() * other.get_denominator()

        return Fraction(new_num, new_denom)

