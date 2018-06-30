# Unittest bootcamp
Describes basics of unittest python testing framework.

## Table of contents
All home works from every chapter will be located in it's `test_home.py` file.
- [Chapter one (write test cases)](#chapter-one-(write-test-cases))
  - [Syntax convention](#syntax-convention)
  - [Basic test case example](#basic-test-case-example)
  - [Run test case(s)](#run-test-case(s))
  - [Assertions](#assertions)
  - [Test case outcomes](#test-case-outcomes)
  - [Run every test case outcome](#run-every-test-case-outcome)
  - [Test case preconditions and postconditions](#test-case-preconditions-and-postconditions)
- [Chapter two (write test suits)](#chapter-two-(write-test-suits))
  - [Basic test suite example](#basic-test-suite-example)
  - [Run test suite](#run-test-case(s))
  - [Prepare test cases for next grouping into test suite](#prepare-test-cases-for-next-grouping-into-test-suite)
  - [Group test cases into one test suite](#group-test-cases-into-one-test-suite)
  - [Group separate tests into one test suite](#group-separate-tests-into-one-test-suite)
  - [Group multiple test suite into one top level test suite](#group-multiple-test-suite-into-one-top-level-test-suite)
  - [Run every grouped test suite](#run-every-grouped-test-suite)
- [Contributing](#contributing)

## Chapter one (write test cases)
This chapter consists basics of unittest test cases usage.
### Syntax convention
```python
# every test module has to start with `test` prefix like `test_item.py`
  
from unittest import TestCase  # import TestCase class object
 
  
class TestScenario(TestCase):  # every test scenario has to start with `Test` prefix
 
    def test_method(self):  # every test method has to start with `test_` prefix
        do_some_assertion()
```
### Basic test case example
```python
# test_list.py

from typing import List
from unittest import TestCase


class TestListMethods(TestCase):
    """ This test case is verifying basic list data type methods. """

    def test_append(self) -> None:
        """ Test checks if given elements are adding to array """

        flist: List[...] = []
        for i in range(1, 4):
            flist.append(i)
        self.assertEqual(flist, [1, 2, 3])

    def test_extend(self) -> None:
        """ Test checks if given elements extends an array """

        flist: List[int] = [1, 2, 3]
        flist.extend(range(4, 6))
        self.assertEqual(flist[-2:], [4, 5])

    def test_insert(self) -> None:
        """ Test checks if given element is inserted into array """

        flist: List[int] = [1, 2, 3]
        flist.insert(3, 4)
        self.assertEqual(flist, [1, 2, 3, 4])

    def test_pop(self) -> None:
        """ Test checks if given element is deleted from an array """

        flist: List[int] = [1, 2, 3]
        flist.pop(1)
        self.assertEqual(flist, [1, 3])
```
### Run test case(s)
```bash
# Run TestListMethods test case in test_list.py test module
~/unittest-bootcamp/chapter_one python -m unittest test_list.TestListMethods -v
  
# Run test_append test method from TestListMethods test case in test_list.py test module
~/unittest-bootcamp/chapter_one python -m unittest test_list.TestListMethods.test_append -v
  
# Run all test cases in test_basic_data_types test module
~/unittest-bootcamp/chapter_one python -m unittest test_list -v
  
# More unittest options
~/unittest-bootcamp/chapter_one python -m unittest -h

```
### Assertions
```python
# test_asserts.py

from unittest import TestCase


class TestAssertion(TestCase):
    """ This test case asserts for truth """

    def test_truth(self) -> None:
        """ Test asserts if object is True or False """

        self.assertTrue(1)
        self.assertFalse(0)

    def test_is(self) -> None:
        """ Test asserts if one object is as an other object """

        self.assertIs('', str())
        self.assertIsNot(4.01, int())

    def test_equals(self) -> None:
        """ Test asserts the equality of two objects """

        self.assertEqual(8.88 / 4, 2.22)
        self.assertNotEqual(8.88 / 4, 2.21)
        self.assertLess(8.88 / 4, 2.23)
        self.assertLessEqual(8.88 / 4, 2.22)
        self.assertGreater(8.88 / 4, 2.21)
        self.assertGreaterEqual(8.88 / 4, 2.22)

    def test_contains(self) -> None:
        """ Test asserts for element membership in given container """

        self.assertIn(1, range(1, 5))
        self.assertNotIn(5, range(1, 5))

    def test_raised_error(self) -> None:
        """ Test asserts for correct raised exception """

        with self.assertRaises(ZeroDivisionError):
            print(1 / 0)

    def test_nones(self) -> None:
        """ Test asserts for None objects  """

        self.assertIsNone(None)
        self.assertIsNotNone(list())

    def test_regexp(self) -> None:
        """ Test asserts for correct regular expression functionality """

        self.assertRegex('400', '\d+')
        self.assertNotRegex('400', '\s+')

    def test_instances(self) -> None:
        """ Test asserts for class instances  """

        class ObjectOne:
            """ Some class object. Overall do nothing  """
            pass

        class ObjectTwo:
            """ Some other class object. Overall do nothing  """
            pass

        obj_one: ObjectOne = ObjectOne()
        obj_two: ObjectTwo = ObjectTwo()

        self.assertIsInstance(obj_one, ObjectOne)
        self.assertNotIsInstance(obj_two, ObjectOne)

    def test_containers(self) -> None:
        """ Test asserts for  correct containers functionality  """

        self.assertSequenceEqual(range(3), (0, 1, 2))
        self.assertListEqual(list(range(3)), [0, 1, 2])
        self.assertTupleEqual(tuple(range(3)), (0, 1, 2))
        self.assertSetEqual(set(range(3)), {0, 1, 2})
        self.assertDictEqual({2: 'two', 1: 'one'}, {1: 'one', 2: 'two'})

```
### Test case outcomes
```python
# test_outcomes.py

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

```
### Run every test case outcome
```bash
# Run basic OK test case
~/unittest-bootcamp/chapter_one python -m unittest test_outcomes.TestOkBasic -v
  
# Run OK test case with skipped tests
~/unittest-bootcamp/chapter_one python -m unittest test_outcomes.TestOkSkip -v
  
# Run OK test case with expected failures tests
~/unittest-bootcamp/chapter_one python -m unittest test_outcomes.TestOkExpectedFailures -v
  
# Run basic FAIL test case with
~/unittest-bootcamp/chapter_one python -m unittest test_outcomes.TestFailBasic -v
  
# Run FAIL test case with error tests
~/unittest-bootcamp/chapter_one python -m unittest test_outcomes.TestFailError -v
  
# Run FAIL test case with unexpected success tests
~/unittest-bootcamp/chapter_one python -m unittest test_outcomes.TestFailUnexpectedSuccess -v
```
### Test case preconditions and postconditions
```python
from unittest import TestCase


def setUpModule():
    """ Setup for a test module """

    print('setUpModule is calling before all test cases in a test module.')

    global module_string
    module_string = 'module string'


def tearDownModule():
    """ Teardown for a test module """

    print('tearDownModule is calling after all test cases in a test module.')


class TestStringMethods(TestCase):
    """ This test case is verifying basic string data type methods for truth. """

    @classmethod
    def setUpClass(cls) -> None:
        """ Setup for current test case. """

        print('setUpClass is calling once before all test methods.')
        cls.class_string: str = 'class string'

    @classmethod
    def tearDownClass(cls) -> None:
        """ Teardown for current test case. """

        print('tearDownClass is calling once after all test methods.')
        del cls.class_string

    def setUp(self):
        """ Setup for every test method. """

        print('setUp is calling before every test method.')
        self.method_string: str = 'method string'

    def tearDown(self) -> None:
        """ Teardown for every test method. """

        print('tearDown is calling after every test method.')
        del self.method_string

    def test_is_title(self) -> None:
        """ Test checks if given string is in titled case """

        print('calling test_is_title')

        titled_module_string: str = module_string.title()
        titled_class_string: str = self.class_string.title()
        titled_method_string: str = self.method_string.title()

        self.assertTrue(titled_module_string.title())
        self.assertTrue(titled_class_string.title())
        self.assertTrue(titled_method_string.istitle())

    def test_is_lower(self) -> None:
        """ Test checks if string is in lower case """

        print('calling test_is_lower')

        lower_module_string: str = module_string.lower()
        lower_class_string: str = self.class_string.lower()
        lower_method_string: str = self.method_string.lower()

        self.assertTrue(lower_module_string.islower())
        self.assertTrue(lower_class_string.islower())
        self.assertTrue(lower_method_string.islower())

    def test_is_upper(self) -> None:
        """ Test checks if string is in upper case """

        print('calling test_is_upper')

        upper_module_string: str = module_string.upper()
        upper_class_string: str = self.class_string.upper()
        upper_method_string: str = self.method_string.upper()

        self.assertTrue(upper_module_string.isupper())
        self.assertTrue(upper_class_string.isupper())
        self.assertTrue(upper_method_string.isupper())
```
## Chapter two (write test suits)
This chapter consists basics of unittest test suits usage.
### Basic test suite example
```python
# test_suite.py module

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
```
### Run test suite
```bash
# Run test suite - test_suite.py test module
~/unittest-bootcamp/chapter_two python test_suite.py
```
### Prepare test cases for next grouping into test suite
```python
# test_filter.py module

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
```
### Group test cases into one test suite
```bash
# test_filter_suite.py module

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
```
### Group separate tests into one test suite
```python
# test_filter_suite_separate_tests.py module

from unittest import TestSuite, TextTestRunner
from chapter_two.test_filter import TestFilterOddNumbers, TestFilterEvenNumbers


def _test_suite() -> TestSuite:
    test_suite: TestSuite = TestSuite()
    for test_case in TestFilterOddNumbers, TestFilterEvenNumbers:
        test_suite.addTest(test_case('test_with_basic_algorithm'))
        test_suite.addTest(test_case('test_with_list_comprehension'))
    return test_suite


if __name__ == '__main__':
    test_runner: TextTestRunner = TextTestRunner(verbosity=2)
    test_runner.run(_test_suite())
```
### Group multiple test suite into one top level test suite
```python
# test_filter_suites.py module

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
```
### Run every grouped test suite
```bash
# Run simple test suite
~/unittest-bootcamp/chapter_two python test_filter_suite.py
  
# Run test suite with separate tests from test cases
~/unittest-bootcamp/chapter_two python test_filter_suite_with_separate_tests.py
  
# Run top level test suite
~/unittest-bootcamp/chapter_two python test_suites.py

```
## Contributing

### Setup
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
