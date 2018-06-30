from typing import List
from unittest import TestCase


class TestFilterOddNumbers(TestCase):
    """ This test case filters odd numbers from a given sequence """

    def test_with_basic_algorithm(self) -> None:
        """ Test checks if odd numbers are filtered with basic algorithm """

        odds: List[...] = list()
        for n in range(1, 6):
            if n % 2 != 0:
                odds.append(n)
        self.assertListEqual(odds, [1, 3, 5])

    def test_with_list_comprehension(self):
        """ Test checks if odd numbers are filtered with list comprehension """

        self.assertListEqual([n for n in range(1, 6) if n % 2 != 0], [1, 3, 5])

    def test_with_filter_function(self) -> None:
        """ Test checks if odd numbers are filtered with 'filter' function """

        def check_odds(n: int) -> bool:
            if not n % 2:
                return False
            return True

        self.assertListEqual(list(filter(check_odds, range(1, 6))), [1, 3, 5])


class TestFilterEvenNumbers(TestCase):
    """ This test case filters even numbers from a given sequence """

    def test_with_basic_algorithm(self) -> None:
        """ Test checks if even numbers are filtered with basic algorithm """

        odds: List[...] = list()
        for n in range(1, 6):
            if n % 2 == 0:
                odds.append(n)
        self.assertListEqual(odds, [2, 4])

    def test_with_list_comprehension(self):
        """ Test checks if even numbers are filtered with list comprehension """

        self.assertListEqual([n for n in range(1, 6) if n % 2 == 0], [2, 4])

    def test_with_filter_function(self) -> None:
        """ Test checks if even numbers are filtered with 'filter' function """

        def check_evens(n: int) -> bool:
            if n % 2:
                return False
            return True

        self.assertListEqual(list(filter(check_evens, range(1, 6))), [2, 4])
