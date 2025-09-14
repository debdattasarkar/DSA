
class Solution:
    def maxWater(self, arr):
        """
        Two-pointer optimized solution (most expected in interviews)
        Time:  O(n)  - each index visited at most once
        Space: O(1)  - constant extra space
        """
        n = len(arr)
        if n < 3:                      # Need at least 3 bars to trap water
            return 0

        l, r = 0, n - 1                # O(1)
        leftMax, rightMax = arr[l], arr[r]
        water = 0

        # Single pass: O(n)
        while l < r:
            # Decide by smaller boundary (it caps the water on that side)
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, arr[l])
                # if leftMax > arr[l], we trap leftMax - arr[l] units at l
                water += max(0, leftMax - arr[l])
            else:
                r -= 1
                rightMax = max(rightMax, arr[r])
                water += max(0, rightMax - arr[r])

        return water