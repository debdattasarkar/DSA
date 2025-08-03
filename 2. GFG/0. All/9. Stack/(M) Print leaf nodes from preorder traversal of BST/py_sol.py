class Solution:
	def leafNodes(self, preorder):
		# code here
		N = len(preorder)
        leafs = []

        def dfs(sta=0, sto=N):
            # Base case: invalid range
            if sta + 1 > sto:
                return
            # Base case: single node in subtree ⇒ it's a leaf
            if sta + 1 == sto:
                leafs.append(preorder[sta])
                return

            # Partition into left (< root) and right (> root)
            ix = sta + 1
            while ix < sto and preorder[ix] < preorder[sta]:
                ix += 1

            # Recurse on left and right partitions
            dfs(sta + 1, ix)  # left subtree
            dfs(ix, sto)      # right subtree

        dfs()
        return leafs 