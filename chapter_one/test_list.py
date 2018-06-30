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
