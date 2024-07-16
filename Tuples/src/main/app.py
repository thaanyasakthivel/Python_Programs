from lab import *

def main():
    # Ask user to enter values for tuple1
    values_str = input("Enter values separated by commas to create tuple1: ")
    values_list = values_str.split(',')
    tuple1 = create_tuple(*values_list)

    # Ask user to enter values for tuple2
    values_str = input("Enter values separated by commas to create tuple2: ")
    values_list = values_str.split(',')
    tuple2 = create_tuple(*values_list)

    # Display tuples
    print("Tuple1:", tuple1)
    print("Tuple2:", tuple2)

    # Access elements
    index = int(input("Enter the index of the element to access in tuple1: "))
    print("Element at index {} in tuple1: {}".format(index, access_element(tuple1, index)))

    # Concatenate tuples
    print("Concatenated tuple:", concatenate_tuples(tuple1, tuple2))

    # Repeat tuple
    n = int(input("Enter the number of times to repeat tuple1: "))
    print("Repeated tuple:", repeat_tuple(tuple1, n))

    # Check membership
    item = input("Enter an item to check membership in tuple1: ")
    print("{} is present in tuple1: {}".format(item, check_membership(tuple1, item)))

    # Check non-membership
    item = input("Enter an item to check non-membership in tuple1: ")
    print("{} is not present in tuple1: {}".format(item, check_non_membership(tuple1, item)))

    # Get tuple length
    print("Length of tuple1:", tuple_length(tuple1))

    # Tuple slicing
    start = int(input("Enter the starting index for slicing tuple1: "))
    end = int(input("Enter the ending index for slicing tuple1: "))
    print("Sliced tuple:", tuple_slicing(tuple1, start, end))

    # Count occurrences
    item = input("Enter an item to count occurrences in tuple1: ")
    print("Number of occurrences of {} in tuple1: {}".format(item, count_occurrences(tuple1, item)))

    # Find index
    item = input("Enter an item to find index in tuple1: ")
    print("Index of {} in tuple1: {}".format(item, find_index(tuple1, item)))


if __name__ == "__main__":
    main()
