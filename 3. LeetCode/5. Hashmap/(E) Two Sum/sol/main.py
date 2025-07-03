from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Create a hashmap (dictionary) to store number → index mapping
        index_map = {}  # key: number, value: index

        # Step 2: Iterate through the array
        for i, num in enumerate(nums):
            # Compute the required complement that would sum to the target
            complement = target - num

            # Step 3: Check if this complement was seen earlier in the hashmap
            if complement in index_map:
                # If yes, return the stored index of the complement and current index
                return [index_map[complement], i]

            # Step 4: If not found, store the current number and its index for future reference
            index_map[num] = i

        # Note: Per the problem, exactly one solution exists, so we never reach here
        return []

nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1]
# Because nums[0] + nums[1] == 2 + 7 = 9

# Execution
sol = Solution()
output = sol.groupAnagrams(nums, target)

# Output (Order may vary)
print(output)