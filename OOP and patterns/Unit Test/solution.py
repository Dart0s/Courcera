import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    """Unit test for the factorize function"""
    def test_wrong_types_raise_exception(self):
        with self.subTest(x='string'):
            self.assertRaises(TypeError, factorize, 'string')
        with self.subTest(x=1.5):
            self.assertRaises(TypeError, factorize, 1.5)

    def test_negative(self):
        self.cases = (-1,  -10,  -100)

        for x in self.cases:
            with self.subTest(x=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        self.cases = ([1, (1,)], [0, (0,)])

        for x in self.cases:
            with self.subTest(x=x[0]):
                self.assertEqual(factorize(x[0]), x[1])

    def test_simple_numbers(self):
        self.cases = ([3, (3,)], [13, (13,)], [29, (29,)])

        for x in self.cases:
            with self.subTest(x=x[0]):
                self.assertEqual(factorize(x[0]), x[1])

    def test_two_simple_multipliers(self):
        self.cases = ([6, (2, 3)],   [26, (2, 13)],   [121, (11, 11)])

        for x in self.cases:
            with self.subTest(x=x[0]):
                self.assertEqual(factorize(x[0]), x[1])

    def test_many_multipliers(self):
        self.cases = ([1001, (7, 11, 13)], [9699690, (2, 3, 5, 7, 11, 13, 17, 19)])

        for x in self.cases:
            with self.subTest(x=x[0]):
                self.assertEqual(factorize(x[0]), x[1])


if __name__ == "__main__":
    unittest.main()
