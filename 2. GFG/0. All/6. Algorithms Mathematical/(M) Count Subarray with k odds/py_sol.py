class Solution:
    def countSubarrays(self, arr, k):
        # prefix_frequency[p] = number of times we've seen odd_prefix == p
        prefix_frequency = {0: 1}  # empty prefix has 0 odds
        odd_prefix = 0
        total_subarrays = 0

        for value in arr:
            # Update prefix odd count
            if value % 2 == 1:
                odd_prefix += 1

            # If previous prefix had (odd_prefix - k), subarray between has k odds
            needed_prefix = odd_prefix - k
            total_subarrays += prefix_frequency.get(needed_prefix, 0)

            # Record current prefix
            prefix_frequency[odd_prefix] = prefix_frequency.get(odd_prefix, 0) + 1

        return total_subarrays