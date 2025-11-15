import bisect
class Solution:
    def rowWithMax1s(self, arr):
        """
        For each row, use binary search to find first 1.
        ones_in_row = m - first_one_index.
        Time : O(n * log m)
        Space: O(1)
        """
        if not arr or not arr[0]:
            return -1

        n, m = len(arr), len(arr[0])
        best_row = -1
        max_ones = 0

        for i in range(n):                      # O(n)
            row = arr[i]
            # first index with value >= 1
            first_one_index = bisect.bisect_left(row, 1)   # O(log m)
            if first_one_index < m:            # row has at least one 1
                ones_in_row = m - first_one_index
                if ones_in_row > max_ones:
                    max_ones = ones_in_row
                    best_row = i

        return best_row if max_ones > 0 else -1