class Solution:
    def countSubarray(self, arr):
        """
        Count subarrays with equal 1s and 0s.

        Trick: map 0 -> -1. Then we need #subarrays with sum == 0.
        Use prefix-sum + hashmap of frequencies.

        Time:  O(n)  (single pass)
        Space: O(n)  (hashmap of prefix sums)
        """
        freq = {0: 1}      # prefix sum 0 seen once (empty prefix)
        s = 0              # running prefix sum over mapped array
        ans = 0

        for x in arr:      # O(n)
            s += 1 if x == 1 else -1   # map 0->-1, 1->+1

            # if s seen k times before, k subarrays ending here have sum 0
            ans += freq.get(s, 0)

            # record the current prefix sum
            freq[s] = freq.get(s, 0) + 1

        return ans