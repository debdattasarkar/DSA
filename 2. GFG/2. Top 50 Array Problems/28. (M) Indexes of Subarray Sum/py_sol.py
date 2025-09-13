#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        l = 0
        curr = 0

        for r in range(n):
            curr += arr[r]                      # expand window

            while l <= r and curr > target:     # shrink until <= target
                curr -= arr[l]
                l += 1

            if curr == target:                  # found earliest such window
                return [l + 1, r + 1]           # 1-based indices

        return [-1]