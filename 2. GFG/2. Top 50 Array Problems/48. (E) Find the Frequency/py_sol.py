"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        """
        Single-pass linear scan (works for any array).
        Time:  O(n)
        Space: O(1)
        """
        cnt = 0
        for v in arr:           # visit each element once
            if v == x:          # O(1) comparison
                cnt += 1
        return cnt