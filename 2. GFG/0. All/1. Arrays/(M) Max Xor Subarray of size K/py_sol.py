class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)

        # XOR of first window
        # Time: O(k), Space: O(1)
        current_window_xor = 0
        for i in range(k):
            current_window_xor ^= arr[i]

        max_window_xor = current_window_xor

        # Slide the window
        # Each move is O(1): remove outgoing, add incoming
        # Time: O(n-k), Space: O(1)
        for right in range(k, n):
            outgoing = arr[right - k]  # element leaving window
            incoming = arr[right]      # element entering window

            current_window_xor ^= outgoing
            current_window_xor ^= incoming

            if current_window_xor > max_window_xor:
                max_window_xor = current_window_xor

        return max_window_xor