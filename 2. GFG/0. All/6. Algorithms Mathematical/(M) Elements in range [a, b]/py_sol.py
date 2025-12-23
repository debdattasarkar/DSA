from bisect import bisect_left, bisect_right
class Solution:
    def cntInRange(self, arr, queries):
        # Sort once so we can binary search ranges quickly
        sorted_arr = sorted(arr)

        results = []
        for left_val, right_val in queries:
            # first position where value >= left_val
            left_index = bisect_left(sorted_arr, left_val)

            # first position where value > right_val
            right_index = bisect_right(sorted_arr, right_val)

            # elements in [left_val, right_val] are within [left_index, right_index)
            results.append(right_index - left_index)

        return results