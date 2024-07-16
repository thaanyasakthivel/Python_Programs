import unittest
from src.main.lab import *


class TestLabFunctions(unittest.TestCase):
    def test_create_tuple(self):
        self.assertEqual(create_tuple(1, 2, 3), (1, 2, 3))

    def test_access_element(self):
        self.assertEqual(access_element((1, 2, 3), 1), 2)

    def test_concatenate_tuples(self):
        self.assertEqual(concatenate_tuples((1, 2), (3, 4)), (1, 2, 3, 4))

    def test_repeat_tuple(self):
        self.assertEqual(repeat_tuple((1, 2), 3), (1, 2, 1, 2, 1, 2))

    def test_check_membership(self):
        self.assertTrue(check_membership((1, 2, 3), 2))
        self.assertFalse(check_membership((1, 2, 3), 4))

    def test_check_non_membership(self):
        self.assertTrue(check_non_membership((1, 2, 3), 4))
        self.assertFalse(check_non_membership((1, 2, 3), 2))

    def test_tuple_length(self):
        self.assertEqual(tuple_length((1, 2, 3)), 3)

    def test_tuple_slicing(self):
        self.assertEqual(tuple_slicing((1, 2, 3, 4, 5), 1, 4), (2, 3, 4))

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences((1, 2, 2, 3, 2), 2), 3)

    def test_find_index(self):
        self.assertEqual(find_index((1, 2, 3, 2, 4), 2), 1)


if __name__ == "__main__":
    unittest.main()
