class Solution:
    def subarrayXor(self, arr):
        """
        Optimized solution using frequency of each element in all subarrays.

        Idea:
        -----
        - Every subarray contributes its XOR.
        - Each element arr[i] appears in many subarrays; exactly:
              count_i = (i + 1) * (n - i)
        - XOR facts:
              x ^ x = 0, x ^ 0 = x
          => if an element appears even times, it cancels;
             if odd times, it contributes once.
        - So final answer is XOR of arr[i] for which count_i is odd.

        Time Complexity:
            O(n) — single pass over array.
        Space Complexity:
            O(1) — only a few variables.
        """
        n = len(arr)
        answer = 0

        for i, value in enumerate(arr):
            # Number of subarrays that include position i
            count = (i + 1) * (n - i)

            # If count is odd, this value contributes once
            if count % 2 == 1:
                answer ^= value

        return answer