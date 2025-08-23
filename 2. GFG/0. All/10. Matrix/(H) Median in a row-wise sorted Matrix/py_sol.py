from bisect import bisect_right

class Solution:
    def median(self, mat):
    	# code here 
    	"""
        Optimal median finder for a row-wise sorted matrix.

        Time:  O(n * log(maxVal-minVal) * log m)
               - For each probe (log range), we count <= mid via bisect in each row (log m)
        Space: O(1)
        """
        n = len(mat)
        m = len(mat[0])

        # 1) Search space is min of first column to max of last column
        low  = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)

        # 2) We want the 1-based index (n*m+1)//2
        need = (n * m + 1) // 2

        # 3) Binary search on value range
        while low < high:
            mid = (low + high) // 2

            # Count elements <= mid using row-wise bisect_right
            cnt = 0
            for row in mat:
                # bisect_right returns index to insert mid on right -> count of <= mid
                cnt += bisect_right(row, mid)

            # If not enough elements <= mid, median is larger
            if cnt < need:
                low = mid + 1
            else:
                high = mid

        return low  # or high (equal here)
