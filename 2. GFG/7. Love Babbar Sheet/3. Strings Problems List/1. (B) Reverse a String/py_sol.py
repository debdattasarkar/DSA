#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        """
        Two-pointer swap on a char list.
        Time:  O(n)   (each index touched ≤ 1 time)
        Space: O(n)   (list + the new output string)
        """
        a = list(s)                  # O(n) to build list of characters
        l, r = 0, len(a) - 1
        while l < r:                 # O(n/2) swaps
            a[l], a[r] = a[r], a[l]
            l += 1; r -= 1
        return ''.join(a)            # O(n) to build result