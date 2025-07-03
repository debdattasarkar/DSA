from typing import List
import timeit

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Convert input list to a set for O(1) lookups
        num_set = set(nums)  # Time: O(n), Space: O(n)
        max_len = 0  # Store the length of the longest consecutive sequence

        # Step 2: Loop through each unique number in the set
        for num in num_set:
            # Start of a new sequence if previous number doesn't exist
            if num - 1 not in num_set:
                current = num
                streak = 1

                # Step 3: Expand the streak forward
                while current + 1 in num_set:
                    current += 1
                    streak += 1

                # Step 4: Update max length found
                max_len = max(max_len, streak)

        return max_len

# Test input
input_data = [100, 4, 200, 1, 3, 2]
solution = Solution()
print("Output:", solution.longestConsecutive(input_data))  # Expected: 4

# Performance check using timeit
def run_solution():
    solution.longestConsecutive(input_data)

execution_time = timeit.timeit(run_solution, number=1000)
print("Execution time for 1000 runs:", execution_time)