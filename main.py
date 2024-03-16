# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# linear search
def linear_search(list, target):
    """
    returns the index positions of the target if found,else return none
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


# write a function called verify that accepts an index value if the value is not none print the index position if it is none inform target wasnt found in the list
def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found at index")


new_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(new_array, 6)
verify(result)


# binary search
def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        mid = (first + last) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found at index")


new_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(new_array, 6)
verify(result)


# recursive binary search
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = len(list) // 2

        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid + 1:], target)
            else:
                return recursive_binary_search(list[:mid], target)


def verify(result):
    print("Target found at index:", result)


new_array = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(new_array, 12)
verify(result)
result = recursive_binary_search(new_array, 6)
verify(result)


