#Initial Template for Python 3
class Solution:
	def ZigZagMaxLength(self, nums):
		"""
        Greedy 2-state DP (up/down).
        Time:  O(n)  – scan once
        Space: O(1)  – two integers
        """
        n = len(nums)
        if n <= 1:
            return n

        up = down = 1  # a single element counts as length 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # extend a 'down' into an 'up'
                up = down + 1
            elif nums[i] < nums[i-1]:
                # extend an 'up' into a 'down'
                down = up + 1
            # else equal: ignore
        return max(up, down)