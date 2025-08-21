'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
    #code here
    # Time: O(n)  — single pass to find the position
        # Space: O(1) — constant extra space
        new_node = Node(x)

        # Case 1: empty list -> new node is the head
        if head is None:
            return new_node

        # Case 2: insert before current head
        if x <= head.data:
            new_node.next = head      # new -> oldHead
            head.prev = new_node      # oldHead <- new
            return new_node           # new head

        # Case 3: insert in middle or tail
        cur = head
        # Walk until first node with value >= x, or end
        while cur is not None and cur.data < x:
            prev = cur
            cur = cur.next

        # Now insert between prev and cur (cur can be None -> tail insert)
        new_node.prev = prev
        new_node.next = cur
        prev.next = new_node
        if cur is not None:
            cur.prev = new_node

        return head