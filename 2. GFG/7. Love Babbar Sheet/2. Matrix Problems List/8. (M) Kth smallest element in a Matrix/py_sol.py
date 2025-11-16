from bisect import bisect_right
class Solution:
    def kthSmallest(self, mat, k):
        """
        Binary search in VALUE space.
        Each row and column are sorted in non-decreasing order.

        Idea:
          - Let low = smallest element, high = largest element.
          - While low < high:
              mid = (low + high) // 2
              count how many elements <= mid
              if count < k:    # not enough small elements
                  low = mid + 1
              else:            # mid is large enough / maybe too large
                  high = mid
          - low (== high) is the k-th smallest element.

        Counting:
          Since each row is sorted, we can use bisect_right(row, mid)
          to get the number of elements <= mid in that row.

        Time  : O(n * log(maxVal - minVal) * log n)  (or O(n log n log V))
        Space : O(1) extra
        """
        n = len(mat)
        if n == 0:
            return None

        # Global minimum and maximum (top-left and bottom-right)
        low = mat[0][0]
        high = mat[-1][-1]

        # Binary search over the value domain
        while low < high:
            mid = (low + high) // 2

            # Count elements <= mid
            count = 0
            for row in mat:
                # bisect_right returns index of first element > mid,
                # which is also count of elements <= mid.
                count += bisect_right(row, mid)

            if count < k:
                # Not enough elements <= mid, need larger values
                low = mid + 1
            else:
                # There are at least k elements <= mid,
                # so k-th smallest is <= mid. Shrink the high bound.
                high = mid

        return low