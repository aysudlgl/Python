from datastructers import LinkedList

def merge_sort(linked_list):
    """
    this function sorts a linked list in ascending order
    -recirsively divide the linked list into sublists containing a single node
    repeatedly merge the sublists to produce sublists until one remains
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(linked_list):
    """
    divide the unsorted list at midpoint sublists
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = linked_list()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half
