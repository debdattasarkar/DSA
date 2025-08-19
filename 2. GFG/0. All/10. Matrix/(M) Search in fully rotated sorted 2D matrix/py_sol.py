class Solution:
    def searchMatrix(self, mat, x):
        # code here
        n = len(mat)
        if n == 0:
            return False
        m = len(mat[0])
        if m == 0:
            return False

        def get(idx):
            i, j = divmod(idx, m)
            return mat[i][j]

        l, r = 0, n * m - 1
        while l <= r:
            mid = (l + r) // 2
            mid_val = get(mid)
            if mid_val == x:
                return True

            left_val, right_val = get(l), get(r)

            # Left half is sorted
            if left_val <= mid_val:
                if left_val <= x < mid_val:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half is sorted
            else:
                if mid_val < x <= right_val:
                    l = mid + 1
                else:
                    r = mid - 1

        return False