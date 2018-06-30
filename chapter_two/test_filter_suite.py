from unittest import TestSuite, TestLoader, TextTestRunner
from chapter_two.test_filter import TestFilterOddNumbers, TestFilterEvenNumbers


def _test_suite() -> TestSuite:
    test_suite: TestSuite = TestSuite()
    for test_case in TestFilterOddNumbers, TestFilterEvenNumbers:
        tests: TestLoader = TestLoader().loadTestsFromTestCase(test_case)
        test_suite.addTests(tests)
    return test_suite


if __name__ == '__main__':
    test_runner: TextTestRunner = TextTestRunner(verbosity=2)
    test_runner.run(_test_suite())
