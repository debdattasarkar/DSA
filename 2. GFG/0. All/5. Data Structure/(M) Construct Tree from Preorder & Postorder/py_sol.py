'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def constructTree(self, pre, post):
        """
        Build a full binary tree from preorder and postorder.
        Assumptions:
          - Full tree (each node has 0 or 2 children)
          - All values are unique; appear in both traversals
        Time  : O(n)  (thanks to O(1) post-index lookups)
        Space : O(n)  (hashmap + recursion stack)
        """
        n = len(pre)
        if n == 0:
            return None

        # Map each value -> its index in post[] for O(1) splits
        idx_in_post = {val: i for i, val in enumerate(post)}

        # 'i' is a moving pointer in preorder (closed over by build())
        self.i = 0

        def build(l, r):
            """
            Rebuilds subtree whose nodes appear somewhere within post[l..r].
            Uses global 'self.i' to pull next root from preorder.
            """
            if l > r:
                return None

            # Create root from preorder
            root_val = pre[self.i]
            self.i += 1
            root = Node(root_val)

            # Leaf node: post[l]..post[r] only contains this root
            if l == r:
                return root

            # Next preorder value must be the left child (since it's full tree)
            left_child_val = pre[self.i]
            # Find how big the left subtree is by where that left child's
            # subtree ends in post (its root appears at idx_in_post[left_child_val])
            mid = idx_in_post[left_child_val]

            # Build left subtree spanning post[l..mid]
            root.left = build(l, mid)
            # Build right subtree spanning post[mid+1..r-1] (r is the current root)
            root.right = build(mid + 1, r - 1)

            return root

        # Entire tree spans post[0..n-1]
        return build(0, n - 1)