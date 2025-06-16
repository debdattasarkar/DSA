from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False  # Stuck before reaching i
            farthest = max(farthest, i + nums[i])  # Extend range
        return True