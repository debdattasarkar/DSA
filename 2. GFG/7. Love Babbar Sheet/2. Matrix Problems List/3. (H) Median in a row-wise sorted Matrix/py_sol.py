from bisect import bisect_right

class Solution:
    def median(self, mat):
    	"""
        Value-space binary search + per-row upper_bound count.
        Time : O(n * log(maxVal - minVal) * log m)
               (for each value guess, do n times bisect_right on length-m rows)
        Space: O(1)
        """
        if not mat or not mat[0]:
            raise ValueError("matrix is empty")

        n, m = len(mat), len(mat[0])

        # global min and max using row-wise facts
        low  = min(row[0]   for row in mat)
        high = max(row[-1]  for row in mat)
        K = (n * m + 1) // 2                         # 1-based median position

        # Binary search smallest value v such that count(<=v) >= K
        while low < high:
            mid = (low + high) // 2

            # Count elements <= mid using bisect_right in each row
            cnt = 0
            for row in mat:
                # number of elements <= mid in this row
                cnt += bisect_right(row, mid)

            if cnt < K:                # not enough small elements, go right
                low = mid + 1
            else:                      # mid is large enough, go left
                high = mid

        return low                     # or high; both equal here