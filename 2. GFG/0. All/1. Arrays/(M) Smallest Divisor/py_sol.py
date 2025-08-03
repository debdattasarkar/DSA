import math

class Solution:
    def smallestDivisor(self, arr, k):
        # Code here
        def is_valid(divisor):
            return sum(math.ceil(x / divisor) for x in arr) <= k

        left, right = 1, max(arr)
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid  # try smaller divisor
            else:
                left = mid + 1  # increase divisor

        return left