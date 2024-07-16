import unittest
from src.main.lab import create_list, access_list_element, reverse_list, combine_lists


class TestLabFunctions(unittest.TestCase):

    def test_create_list_positive(self):
        # Test for a positive number of elements
        self.assertEqual(create_list(5), [1, 2, 3, 4, 5])

    def test_create_list_zero(self):
        # Test for zero elements
        with self.assertRaises(ValueError) as context:
            create_list(0)
        self.assertEqual(str(context.exception), "Number of elements must be positive")

    def test_create_list_negative(self):
        # Test for a negative number of elements
        with self.assertRaises(ValueError) as context:
            create_list(-5)
        self.assertEqual(str(context.exception), "Number of elements must be positive")


    def test_access_list_element(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(access_list_element(test_list, 2), 3)
        self.assertEqual(access_list_element(test_list, 5), "Invalid index")
        self.assertEqual(access_list_element(test_list, -1), "Invalid index")

    def test_reverse_list(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(reverse_list(test_list), [5, 4, 3, 2, 1])

    def test_combine_lists(self):
        list1 = [1, 2, 3]
        list2 = [4, 5]
        self.assertEqual(combine_lists(list1, list2), [1, 2, 3, 4, 5])


if __name__ == '__main__': 
    unittest.main()
