def create_list(n):
    """
    Instead of returning 0, this method should Create a list of numbers from 1 to n and return it.

    :param n: The number of elements in the list.
    :return: The created list.

    Instructions:
    --------------
    1. Use the `range()` function to generate a list of numbers from 1 to `n`.
    2. Ensure that the function handles the case when `n` is 0 or negative.
    """
    if n <= 0:
        raise ValueError("Number of elements must be positive")
    return 0


def access_list_element(my_list, index):
    """
    Instead of returning None , this method should be able to access a single element of the list and return it along with its index.

    :param my_list: The list to access elements from.
    :param index: The index of the element to access.
    :return:  the element at the given index.
    """
    if index < 0 or index >= len(my_list):
        return "Invalid index"
    
    return -1


def reverse_list(my_list):
    """
    Instead of returning 0, it should return the reverse of the list.

    :param my_list: The list to reverse.
    :return: The reversed list.
    """
    return 0


def combine_lists(list1, list2):
    """
    Instead of returning 0, this method should Combine two lists and return the combined list.

    :param list1: The first list.
    :param list2: The second list.
    :return: The combined list.
    """
    return 0


