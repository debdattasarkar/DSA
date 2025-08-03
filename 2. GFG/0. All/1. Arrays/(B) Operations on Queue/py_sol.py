from collections import deque

#User function Template for python3
class Solution:
    def enqueue(self, q, x):
        # code here
        q.append(x)  # O(1) append to rear

    def dequeue(self, q):
        # code here
        return q.popleft() if q else -1  # O(1) pop from front

    def front(self, q):
        # code here
        return q[0] if q else -1  # O(1) peek front

    def find(self, q, x):
        # code here
        return x in q  # O(n) linear search