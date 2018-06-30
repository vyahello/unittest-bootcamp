from typing import List
from unittest import TestCase, expectedFailure, skip


class TestOkBasic(TestCase):
    """ Basic OK test case outcome """

    def test_odd_numbers_with_basic_algorithm(self) -> None:
        """ Test checks if odd numbers are filtered with basic algorithm """

        odds: List[...] = list()
        for n in range(1, 6):
            if n % 2 != 0:
                odds.append(n)
        self.assertListEqual(odds, [1, 3, 5])

    def test_odd_numbers_with_list_comprehension(self) -> None:
        """ Test checks if odd numbers are filtered with list comprehension """

        self.assertListEqual([n for n in range(1, 6) if n % 2 != 0], [1, 3, 5])


class TestOkSkip(TestCase):
    """ OK test case outcome with skipped tests """

    @skip('Skip test without any condition')
    def test_odd_numbers_with_basic_algorithm(self) -> None:
        """ Test checks if odd numbers are filtered with basic algorithm """

        odds: List[...] = list()
        for n in range(1, 6):
            if n % 2 != 0:
                odds.append(n)
        self.assertListEqual(odds, [1, 3, 5])

    def test_odd_numbers_with_list_comprehension(self) -> None:
        """ Test checks if odd numbers are filtered with list comprehension """

        self.skipTest('I want to skip this test')
        self.assertListEqual([n for n in range(1, 6) if n % 2 != 0], [1, 3, 5])


class TestOkExpectedFailures(TestCase):
    """ OK test case outcome with expected failures """

    @expectedFailure
    def test_with_basic_algorithm(self) -> None:
        """ Test checks if odd numbers are filtered with basic algorithm """

        odds: List[...] = list()
        for n in range(1, 6):
            if n % 2 != 0:
                odds.append(n)
        self.assertListEqual(odds, None)

    @expectedFailure
    def test_with_list_comprehension(self) -> None:
        """ Test checks if odd numbers are filtered with list comprehension """

        self.assertListEqual([n for n in range(1, 6) if n % 2 != 0], None)


class TestFailBasic(TestCase):
    """ Basic FAIL test case outcome """

    def test_with_basic_algorithm(self) -> None:
        """ Test checks if odd numbers are filtered with basic algorithm """

        odds: List[...] = list()
        for n in range(1, 6):
            if n % 2 != 0:
                odds.append(n)
        self.assertListEqual(odds, None)

    def test_with_list_comprehension(self) -> None:
        """ Test checks if odd numbers are filtered with list comprehension """

        self.assertListEqual([n for n in range(1, 6) if n % 2 != 0], None)


class TestFailError(TestCase):
    """ FAIL test case outcome with error tests """

    def test_with_basic_algorithm(self) -> None:
        """ Test checks if odd numbers are filtered with basic algorithm """

        odds: List[...] = list()
        for n in range(1, 6):
            if n % 2 != 0:
                odds.append(n)
        self.assertListEqual(odds)

    def test_with_list_comprehension(self) -> None:
        """ Test checks if odd numbers are filtered with list comprehension """

        self.assertListEqual([n for n in range(1, 6) if n % 2 != 0])


class TestFailUnexpectedSuccess(TestCase):
    """ FAIL test case outcome with unexpected success tests """

    @expectedFailure
    def test_with_basic_algorithm(self) -> None:
        """ Test checks if odd numbers are filtered with basic algorithm """

        odds: List[...] = list()
        for n in range(1, 6):
            if n % 2 != 0:
                odds.append(n)
        self.assertListEqual(odds, [1, 3, 5])

    @expectedFailure
    def test_with_list_comprehension(self) -> None:
        """ Test checks if odd numbers are filtered with list comprehension """

        self.assertListEqual([n for n in range(1, 6) if n % 2 != 0], [1, 3, 5])
