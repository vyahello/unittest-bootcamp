from unittest import TestSuite, TextTestRunner
from chapter_two.test_filter import TestFilterOddNumbers, TestFilterEvenNumbers


def _test_suite() -> TestSuite:
    test_suite = TestSuite()
    for test_case in TestFilterOddNumbers, TestFilterEvenNumbers:
        test_suite.addTest(test_case('test_with_basic_algorithm'))
        test_suite.addTest(test_case('test_with_list_comprehension'))
    return test_suite


if __name__ == '__main__':
    test_runner: TextTestRunner = TextTestRunner(verbosity=2)
    test_runner.run(_test_suite())
