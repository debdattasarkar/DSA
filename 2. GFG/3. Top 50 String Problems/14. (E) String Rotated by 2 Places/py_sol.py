class Solution:
    def isRotated(self,s1,s2):
        """
        Check if s2 equals s1 rotated by exactly 2 positions (either direction).
        Time : O(n)  — slicing is linear in string length
        Space: O(n)  — new strings from slices
        """
        # Length mismatch = impossible
        if len(s1) != len(s2):
            return False

        n = len(s1)
        # For strings of length < 2, a 2-rotation does nothing
        if n < 2:
            return s1 == s2

        left2  = s1[2:] + s1[:2]   # rotate left by 2
        right2 = s1[-2:] + s1[:-2] # rotate right by 2

        return s2 == left2 or s2 == right2