class Solution:
    def subarraySum(self, arr):
        # code here 
        n = len(arr)
        total = 0

        for i in range(n):
            # Each element contributes to (i+1)*(n-i) subarrays
            contribution = arr[i] * (i + 1) * (n - i)
            total += contribution

        return total