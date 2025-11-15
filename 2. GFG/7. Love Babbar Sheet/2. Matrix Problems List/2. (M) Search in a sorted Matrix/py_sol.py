class Solution:
    def searchMatrix(self, mat, x): 
    	"""
        Binary search treating matrix as 1-D sorted array.
        Map mid -> (mid//m, mid%m).
        Time:  O(log(n*m))
        Space: O(1)
        """
        if not mat or not mat[0]:
            return False
        n, m = len(mat), len(mat[0])

        left, right = 0, n * m - 1
        while left <= right:
            mid = (left + right) // 2
            r, c = divmod(mid, m)       # r=mid//m, c=mid%m
            val = mat[r][c]
            if val == x:
                return True
            if val < x:
                left = mid + 1
            else:
                right = mid - 1
        return False