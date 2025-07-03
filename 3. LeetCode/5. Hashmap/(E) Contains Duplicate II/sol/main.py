import timeit
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}  # Dictionary to store the last seen index of each number

        for i, num in enumerate(nums):
            # If the number is already seen and the index difference is within k
            if num in index_map and i - index_map[num] <= k:
                return True  # Nearby duplicate found
            # Update the index of the current number
            index_map[num] = i

        return False  # No such pair found

# Example input
nums = [1, 2, 3, 1]
k = 3

# Instantiate solution class
sol = Solution()

# Execute and print result
output = sol.containsNearbyDuplicate(nums, k)
print("Output:", output)  # Expected: True

# --- Timeit wrapper ---
def run_solution():
    sol.containsNearbyDuplicate(nums, k)

# Measure time taken for 1000 runs
execution_time = timeit.timeit(run_solution, number=1000)
print("Execution time for 1000 runs:", execution_time, "seconds")