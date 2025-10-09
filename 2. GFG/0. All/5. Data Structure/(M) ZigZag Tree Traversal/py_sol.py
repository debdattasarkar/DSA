'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def zigZagTraversal(self, root):
        # Edge case
        if not root:
            return []
        
        q = deque([root])          # queue for BFS; O(n) worst-case space
        left_to_right = True
        ans = []                   # final output; O(n) space
        
        # Each node is enqueued and dequeued exactly once -> O(n) time
        while q:
            level_size = len(q)    # number of nodes at this level
            level = deque()        # collect values for this level with O(1) appendleft/append
            
            for _ in range(level_size):
                node = q.popleft()               # O(1)
                
                # Direction-aware placement (avoid per-level reverse)
                if left_to_right:
                    level.append(node.data)      # O(1)
                else:
                    level.appendleft(node.data)  # O(1)
                
                # Standard BFS enqueues: always left then right (direction does not affect enqueuing)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Append this level to answer
            ans.extend(level)       # O(width) per level; total O(n)
            left_to_right = not left_to_right
        
        # Total: Time O(n), Space O(n) (queue + output)
        return ans