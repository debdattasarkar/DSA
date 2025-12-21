from bisect import bisect_left, bisect_right
class Solution:
    def countXInRange(self, arr, queries):
        """
        Optimized using binary search (lower_bound & upper_bound).

        For each query [l, r, x]:
            left_index  = first position of x in arr[l..r]  (lower_bound)
            right_index = first position > x in arr[l..r]   (upper_bound)
            count = right_index - left_index

        Time:  O(q * log n)
        Space: O(1)
        """
        answers = []

        for left, right, target in queries:
            # bisect functions allow searching within a subrange:
            # lo = left, hi = right+1 (because hi is exclusive)
            first_ge = bisect_left(arr, target, left, right + 1)
            first_gt = bisect_right(arr, target, left, right + 1)

            answers.append(first_gt - first_ge)

        return answers