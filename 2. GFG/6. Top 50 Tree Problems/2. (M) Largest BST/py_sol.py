class Solution:
    def largestBst(self, root):
        self.best = 0  # tracks largest BST size found
        
        def dfs(node):
            """
            Returns a tuple:
            (is_bst, size, min_val, max_val)
            
            - is_bst: whether the subtree rooted at node is a BST
            - size:   if BST -> size of this BST; if not, any value (we won't use)
            - min_val, max_val: bounds of this subtree when it's a BST
            """
            if not node:
                # Empty subtree is a BST of size 0 and neutral bounds
                return True, 0, float('inf'), float('-inf')
            
            l_is, l_sz, l_min, l_max = dfs(node.left)
            r_is, r_sz, r_min, r_max = dfs(node.right)
            
            # Check BST validity at this node
            if l_is and r_is and l_max < node.data < r_min:
                sz = l_sz + r_sz + 1
                self.best = max(self.best, sz)
                # New bounds for this BST
                mn = min(l_min, node.data)
                mx = max(r_max, node.data)
                return True, sz, mn, mx
            else:
                # Not a BST here, return a marker that prevents parent from forming a BST
                return False, 0, 0, 0
        
        dfs(root)
        return self.best