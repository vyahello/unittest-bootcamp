from unittest import TestSuite, TestLoader, TextTestRunner
from chapter_two.test_filter import TestFilterOddNumbers, TestFilterEvenNumbers


def _test_suite() -> TestSuite:
    filter_odds_suite: TestLoader = TestLoader().loadTestsFromTestCase(TestFilterOddNumbers)
    filter_evens_suite: TestLoader = TestLoader().loadTestsFromTestCase(TestFilterEvenNumbers)
    top_filter_suite: TestSuite = TestSuite([filter_odds_suite, filter_evens_suite])
    return top_filter_suite


if __name__ == '__main__':
    test_runner: TextTestRunner = TextTestRunner(verbosity=2)
    test_runner.run(_test_suite())