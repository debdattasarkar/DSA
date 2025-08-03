# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum = 0
        sum_map = {}
        max_len = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_len = i + 1

            if prefix_sum - k in sum_map:
                max_len = max(max_len, i - sum_map[prefix_sum - k])

            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i  # Store first occurrence only

        return max_len
