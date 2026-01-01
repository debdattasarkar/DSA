'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        # Store references of all nodes from list1
        visited_nodes = set()

        current = head1
        while current:
            visited_nodes.add(current)   # store node identity (reference)
            current = current.next

        # First node in list2 that is already seen is intersection
        current = head2
        while current:
            if current in visited_nodes:
                return current           # return Node (NOT current.data)
            current = current.next

        return None  # problem says intersection always exists