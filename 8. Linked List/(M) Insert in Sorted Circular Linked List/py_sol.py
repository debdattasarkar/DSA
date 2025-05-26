class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # If the list is empty
        if head is None:
            new_node.next = new_node
            return new_node

        current = head

        # Case: insert before head (smallest value)
        if data < head.data:
            # Find last node
            while current.next != head:
                current = current.next

            current.next = new_node
            new_node.next = head
            return new_node  # new head

        # General case: insert in proper place
        current = head
        while current.next != head and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return head