def get_middle_node(head):

    # Create two pointers, slow and fast ,initially pointing to the head
    slow = head
    fast = head

    # Traverse the linked list until fast reaches at the last node or NULL
    while fast and fast.next:

        # Move slow pointer one step ahead
        slow = slow.next

        # Move fast pointer two steps ahead
        fast = fast.next.next

    # Return the slow pointer
    return slow

# Driver code
def main():

    input = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
    )

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(i+1, ".\tLinked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tMiddle of the linked list: ",
              get_middle_node(input_linked_list.head).val)
        print("-"*100, "\n")

if __name__ == "__main__":
    main()