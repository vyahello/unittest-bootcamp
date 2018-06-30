from unittest import TestSuite, TestLoader, TextTestRunner
from chapter_one.test_list import TestListMethods  # use test_list.py module from `Basic test case example` section in `chapter_one` puzzle


def _test_suite() -> TestSuite:
    test_suite: TestSuite = TestSuite()
    tests :TestLoader = TestLoader().loadTestsFromTestCase(TestListMethods)
    test_suite.addTests(tests)
    return test_suite


if __name__ == '__main__':
    test_runner: TextTestRunner = TextTestRunner(verbosity=2)
    test_runner.run(_test_suite())
