class Solution:
    def getLastMoment(self, n, left, right):
        """
        Time Complexity: O(n)  — where n = max(len(left), len(right))
        Space Complexity: O(1) — No extra space used apart from constants
        """
        # Max time for ants going left is their distance from 0
        left_max = max(left) if left else 0
        
        # Max time for ants going right is their distance from n
        right_max = n - min(right) if right else 0
        
        # The ant that takes longest to fall off
        return max(left_max, right_max)