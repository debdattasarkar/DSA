from collections import defaultdict

class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        # HashMap to store frequency of prefix sums
        prefix_map = defaultdict(int)
        prefix_map[0] = 1  # to handle subarrays that sum to k from index 0

        curr_sum = 0
        count = 0

        for num in arr:
            curr_sum += num

            # If (curr_sum - k) exists, we found a subarray
            if (curr_sum - k) in prefix_map:
                count += prefix_map[curr_sum - k]

            # Store current prefix sum in map
            prefix_map[curr_sum] += 1

        return count