from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        # code here
        b.sort()  # Sort b once
        na = len(a)
        nb = len(b)
        freq = [0] * na
        i = 0
        for val in a:
            # bisect_right returns the number of elements ≤ val
            freq[i] = bisect_right(b, val)
            i += 1
            
        return freq