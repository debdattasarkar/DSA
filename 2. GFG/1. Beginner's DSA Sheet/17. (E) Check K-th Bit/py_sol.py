class Solution:
    def checkKthBit(self, n, k):
        # code here
        """
        Idiomatic bitwise solution (mask & AND).
        Time: O(1), Space: O(1)
        """
        # Build a mask with only k-th bit set: 1 << k
        # AND with n — if nonzero, the k-th bit in n was 1.
        return (n & (1 << k)) != 0