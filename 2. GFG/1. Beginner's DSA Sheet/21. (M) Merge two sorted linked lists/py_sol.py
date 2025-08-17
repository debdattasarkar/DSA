
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None


class Solution:
    def sortedMerge(self,head1, head2):
        # Create a dummy node to serve as the starting point
        dummy = Node(-1)
        tail = dummy  # Tail will track the last node in the result list

        # Merge while both lists have nodes
        while head1 and head2:
            if head1.data < head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next  # Move the tail

        # If either list still has nodes, append it
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2

        # Return the merged list starting from dummy.next
        return dummy.next