def recursion(lst):
    if not lst:  # Base case: if the list is empty
        return ""
    else:
        return str(len(lst)) + "," + recursion(lst[:-1])  # Recursively count elements and concatenate them

def main():
    new_array = list(map(int, input("Enter the list of integers separated by commas: ").split(',')))
    print("Number of elements (counting backwards):", recursion(new_array))

main()
