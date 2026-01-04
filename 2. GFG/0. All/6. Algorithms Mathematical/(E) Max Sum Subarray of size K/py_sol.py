class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)

        # Compute sum of first window of size k
        # Time: O(k), Space: O(1)
        current_window_sum = 0
        for i in range(k):
            current_window_sum += arr[i]

        max_window_sum = current_window_sum

        # Slide window from index k to n-1
        # Each step: remove arr[i-k], add arr[i]
        # Time: O(n-k), Space: O(1)
        for right in range(k, n):
            element_entering = arr[right]
            element_leaving = arr[right - k]

            current_window_sum = current_window_sum - element_leaving + element_entering
            if current_window_sum > max_window_sum:
                max_window_sum = current_window_sum

        return max_window_sum