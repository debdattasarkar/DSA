from collections import deque

class Solution:
    def generateBinary(self, n):
        """
        Queue/BFS approach: generate strings in increasing order by expanding each node to x0, x1.
        Time  : O(n)   (we pop/push constant work per item)
        Space : O(n)   (queue + result)
        """
        if n <= 0:
            return []
        
        res = []
        q = deque()
        q.append("1")  # start from 1
        
        for _ in range(n):
            cur = q.popleft()     # the next binary number
            res.append(cur)
            q.append(cur + "0")   # generate next two numbers in sequence
            q.append(cur + "1")
        
        return res