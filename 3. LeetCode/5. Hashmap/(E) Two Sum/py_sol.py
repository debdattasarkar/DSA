class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}  # Stores num → index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement], i]  # Return indices
            index_map[num] = i  # Store index of current num