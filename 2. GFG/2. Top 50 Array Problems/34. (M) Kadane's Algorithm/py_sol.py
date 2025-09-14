class Solution:
    def maxSubarraySum(self, arr):
        # Kadane's algorithm
        # Time:  O(n) — single pass
        # Space: O(1) — constant extra space
        cur = best = arr[0]             # init with first element to handle all-negatives
        for x in arr[1:]:
            cur = max(x, cur + x)       # either extend previous or start fresh at x
            best = max(best, cur)       # track the global best
        return best