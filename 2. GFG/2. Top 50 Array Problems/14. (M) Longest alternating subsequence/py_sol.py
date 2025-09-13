#User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        """
        Greedy wiggle DP in O(n) time, O(1) space.
        up   = best LAS length ending here where the last step went up
        down = best LAS length ending here where the last step went down
        """
        n = len(arr)
        if n == 0: 
            return 0
        # Single element is trivially alternating
        up = down = 1
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                # We can extend a "down" by going up
                up = down + 1
            elif arr[i] < arr[i - 1]:
                # We can extend an "up" by going down
                down = up + 1
            # else: equal -> ignore; no change
        
        return max(up, down)