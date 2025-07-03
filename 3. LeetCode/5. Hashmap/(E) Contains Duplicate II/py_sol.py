class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True  # Found previous occurrence within distance k
            index_map[num] = i  # Update last index

        return False