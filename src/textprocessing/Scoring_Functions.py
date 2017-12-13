import nltk.metrics as nm
#
class Scoring_Functions():
    #
    def __init__(self):
        pass
    #
    def accuracy(self, reference, test):
        """
        Given a list of reference values and a corresponding list of test
        values, return the fraction of corresponding values that are
        equal.  In particular, return the fraction of indices
        ``0<i<=len(test)`` such that ``test[i] == reference[i]``.

        :type reference: list
        :param reference: An ordered list of reference values.
        :type test: list
        :param test: A list of values to compare against the corresponding
            reference values.
        :raise ValueError: If ``reference`` and ``length`` do not have the
            same length.
        """
        if len(reference) != len(test):
            raise ValueError("Lists must have the same length.")
        return sum(x == y for x, y in zip(reference, test)) / len(test)
    #
    def precision(self, reference, test):
        """
        Given a set of reference values and a set of test values, return
        the fraction of test values that appear in the reference set.
        In particular, return card(``reference`` intersection ``test``)/card(``test``).
        If ``test`` is empty, then return None.

        :type reference: set
        :param reference: A set of reference values.
        :type test: set
        :param test: A set of values to compare against the reference set.
        :rtype: float or None
        """
        if (not hasattr(reference, 'intersection') or
                not hasattr(test, 'intersection')):
            raise TypeError('reference and test should be sets')

        if len(test) == 0:
            return None
        else:
            return len(reference.intersection(test)) / len(test)
    #
    def recall(self, reference, test):
        """
        Given a set of reference values and a set of test values, return
        the fraction of reference values that appear in the test set.
        In particular, return card(``reference`` intersection ``test``)/card(``reference``).
        If ``reference`` is empty, then return None.

        :type reference: set
        :param reference: A set of reference values.
        :type test: set
        :param test: A set of values to compare against the reference set.
        :rtype: float or None
        """
        if (not hasattr(reference, 'intersection') or
                not hasattr(test, 'intersection')):
            raise TypeError('reference and test should be sets')

        if len(reference) == 0:
            return None
        else:
            return len(reference.intersection(test)) / len(reference)
    #
    def f_measure(self, reference, test, alpha=0.5):
        """
        Given a set of reference values and a set of test values, return
        the f-measure of the test values, when compared against the
        reference values.  The f-measure is the harmonic mean of the
        ``precision`` and ``recall``, weighted by ``alpha``.  In particular,
        given the precision *p* and recall *r* defined by:

        - *p* = card(``reference`` intersection ``test``)/card(``test``)
        - *r* = card(``reference`` intersection ``test``)/card(``reference``)

        The f-measure is:

        - *1/(alpha/p + (1-alpha)/r)*

        If either ``reference`` or ``test`` is empty, then ``f_measure``
        returns None.

        :type reference: set
        :param reference: A set of reference values.
        :type test: set
        :param test: A set of values to compare against the reference set.
        :rtype: float or None
        """
        p = self.precision(reference, test)
        r = self.recall(reference, test)
        if p is None or r is None:
            return None
        if p == 0 or r == 0:
            return 0
        return 1.0 / (alpha / p + (1 - alpha) / r)