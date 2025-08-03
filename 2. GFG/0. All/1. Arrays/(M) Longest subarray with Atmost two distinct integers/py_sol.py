class Solution:
    def totalElements(self, arr):
        # Code here
        from collections import defaultdict

        left = 0
        max_len = 0
        freq = defaultdict(int)

        for right in range(len(arr)):
            freq[arr[right]] += 1

            # Shrink window if more than 2 distinct
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len