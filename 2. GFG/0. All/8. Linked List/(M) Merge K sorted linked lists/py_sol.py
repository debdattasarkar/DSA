'''
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''
import heapq
class Solution:
    def mergeKLists(self, arr):
        # code here
        """
        Merge k sorted linked lists using a min-heap of size at most k.
        Time:  O(N log k)  (N total nodes)
        Space: O(k)        (heap holds at most one node per list)
        """
        # Edge case: no lists
        if not arr:
            return None

        # Min-heap entries are tuples: (node_value, unique_id, node)
        # unique_id breaks ties so Python doesn't need to compare Node objects.
        heap = []
        uid = 0
        for head in arr:
            if head:  # skip empty lists
                heapq.heappush(heap, (head.data, uid, head))
                uid += 1

        dummy = Node(0)  # sentinel to build the result easily
        tail = dummy

        while heap:
            _, _, node = heapq.heappop(heap)  # smallest node
            tail.next = node                  # append this node
            tail = tail.next                  # advance tail

            if node.next:                     # push next node from same list
                heapq.heappush(heap, (node.next.data, uid, node.next))
                uid += 1

        tail.next = None  # ensure the merged list terminates
        return dummy.next