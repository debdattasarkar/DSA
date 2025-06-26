from linked_list import LinkedList
from print_list import print_list_with_forward_arrow

def remove_nth_last_node(head, n):
    # Point two pointers, right and left, at head.
    right = head
    left = head

    # Move right pointer n elements away from the left pointer.
    for i in range(n):
        right = right.next
    
    # Removal of the head node.
    if not right:
        return head.next
    
    # Move both pointers until right pointer reaches the last node.
    while right.next:
        right = right.next
        left = left.next

        # At this point, left pointer points to (n-1)th element.
        # So link it to next to next element of left.
    left.next = left.next.next

    return head

# Driver code
def main():
    lists = [[23, 89, 10, 5, 67, 39, 70, 28], [34, 53, 6, 95, 38, 28, 17, 63, 16, 76], [288, 224, 275, 390, 4, 383, 330, 60, 193],
    [1, 2, 3, 4, 5, 6, 7, 8, 9], [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]]
    n = [4, 1, 6, 9, 11]

    for i in range(len(n)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lists[i])
        print(i+1, ". Linked List:\t", end='')
        print_list_with_forward_arrow(input_linked_list.head)
        print()
        print("n = ", n[i])
        result = remove_nth_last_node(input_linked_list.head, n[i])
        print("Updated Linked List:\t", end='')
        print_list_with_forward_arrow(result)
        print()
        print("-"*100)

if __name__ == '__main__':
    main()