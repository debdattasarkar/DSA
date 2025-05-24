class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        n = len(arr)
        start = 0
        curr_sum = 0
        min_len = float('inf')

        for end in range(n):
            curr_sum += arr[end]

            while curr_sum > x:
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1

        return min_len if min_len != float('inf') else 0
