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
