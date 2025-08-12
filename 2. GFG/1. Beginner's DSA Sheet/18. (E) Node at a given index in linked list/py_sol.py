"""index is the node which is to be displayed in output
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
class Solution:
    def GetNth(self, head, index):
        # Code Here
        # Guard for invalid index (<= 0)
        if index <= 0:
            return -1  # O(1) time/space
        
        curr = head    # O(1) space
        pos  = 1       # current 1-based position
        
        # Traverse until we either hit the index or run out of nodes
        while curr is not None and pos < index:  # Each loop is O(1); total O(n)
            curr = curr.next
            pos += 1
        
        # If we stopped because we reached the desired position, return data
        if curr is not None and pos == index:
            return curr.data  # Found; O(1)
        
        # Otherwise, index is out of bounds
        return -1  # O(1)