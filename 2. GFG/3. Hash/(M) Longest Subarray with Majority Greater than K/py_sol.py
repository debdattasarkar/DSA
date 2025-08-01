class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        # Step 1: Transform the array into +1 and -1
        n = len(arr)
        nums = [1 if num > k else -1 for num in arr]

        # Step 2: Use prefix sum and a hash map to track first seen positions
        prefix_sum = 0
        first_occurrence = {}  # stores earliest index for each prefix sum
        max_len = 0

        for i in range(n):
            prefix_sum += nums[i]

            # Case 1: total sum is positive → whole subarray [0..i] is valid
            if prefix_sum > 0:
                max_len = i + 1

            # Case 2: check if prefix_sum - 1 occurred before
            if prefix_sum - 1 in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix_sum - 1])

            # Store the first occurrence only
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len