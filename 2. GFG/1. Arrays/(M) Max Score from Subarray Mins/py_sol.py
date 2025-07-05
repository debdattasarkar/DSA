class Solution:
    def maxSum(self, arr):
        ans = float('-inf')  # Start with the smallest number possible

        # Loop through the array until the second last element
        for i in range(len(arr) - 1):
            # Check the sum of the current and next element
            pair_sum = arr[i] + arr[i + 1]

            # Update the max if this pair sum is greater
            if pair_sum > ans:
                ans = pair_sum

        return ans  # Return the max sum found