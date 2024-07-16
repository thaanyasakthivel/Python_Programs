from lab import *


def main():

    # Create a list of numbers from 1 to n
    n = int(input("Enter the number of elements for the list: "))
    num_list = create_list(n)
    print("List of numbers:", num_list)

    # Access the element at the given index 
    
    my_list=[1,2,3,4,5,6,7,8,9,10]
    print("The sample list:",my_list)
    index = int(input("Enter the index of the element to access from this my_list: "))
    element= access_list_element(my_list, index)
    if element is not None:
        print(f"Element at index {index}: {element}")
    else:
        print("Invalid index")


    # Reverse the list
    print("\nReversing the list:")
    reversed_list = reverse_list(num_list)
    print("Reversed list:", reversed_list)

    # Combine two lists
    list1 = [6, 7, 8]
    list2 = [9, 10]
    print("\nCombining two lists:")
    combined_list = combine_lists(list1, list2)
    print("Combined list:", combined_list)




if __name__ == "__main__":
    main()