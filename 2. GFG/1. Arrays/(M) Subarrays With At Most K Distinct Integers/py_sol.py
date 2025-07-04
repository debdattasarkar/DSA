from collections import defaultdict
class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        freq = defaultdict(int)
        left = 0
        count = 0

        for right in range(len(arr)):
            # If it's a new element, reduce k
            if freq[arr[right]] == 0:
                k -= 1
            freq[arr[right]] += 1

            # Shrink window until distinct <= k
            while k < 0:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    k += 1
                left += 1

            # Add number of subarrays ending at `right`
            count += (right - left + 1)

        return count