__author__ = 'Scott'

class Fraction:
    def __init__(self, num, denom):
        self._num = 0
        self._denom = 1
        self.set_numerator(num)
        self.set_denominator(denom)

        return

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
        # NEXT CREATE TESTS
        raise NotImplementedError

    def __eq__(self, other):
        """
        :param other: another Fraction
        :return: True if fractions reduced are the same, otherwise False
        """
        assert isinstance(other, Fraction), 'must only compare Fractions'
        raise NotImplementedError

