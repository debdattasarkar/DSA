class Solution:
    def rowWithMax1s(self, arr):
        """
        Staircase walk from top-right.
        Time : O(n + m)   (each step moves either left or down)
        Space: O(1)
        Returns: index of first row having the maximum number of 1s, else -1.
        """
        if not arr or not arr[0]:
            return -1

        n, m = len(arr), len(arr[0])
        i, j = 0, m - 1
        best_row = -1

        while i < n and j >= 0:
            if arr[i][j] == 1:
                # Found a 1: this row beats all rows seen so far at column j..m-1.
                best_row = i
                j -= 1                  # move left to try to find even more 1s here
            else:
                # Found a 0: this row has 0s up to j, can't improve here -> go down.
                i += 1

        return best_row