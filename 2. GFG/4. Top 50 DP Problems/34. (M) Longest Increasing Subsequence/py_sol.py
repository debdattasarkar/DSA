from bisect import bisect_left
class Solution:
    def lis(self, arr):
        """
        O(n log n) patience-sorting style solution (length only).
        tails[i] = minimum possible tail of any increasing subsequence of length i+1.
        For each x:
          - pos = first index with tails[pos] >= x   (bisect_left for STRICTLY increasing)
          - if pos == len(tails): append x (extend LIS)
            else: replace tails[pos] = x (improve tail)
        Time:  O(n log n)
        Space: O(n)  (tails)
        """
        if not arr:
            return 0

        tails = []
        for x in arr:
            pos = bisect_left(tails, x)   # first >= x
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        return len(tails)
