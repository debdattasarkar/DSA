#User function Template for python3

class Solution:
    def rotate(self, arr):
        """
        Rotate array right by 1 (clockwise) in-place.
        Time:  O(n)  -- single backward pass
        Space: O(1)  -- only one temp
        """
        n = len(arr)
        if n <= 1:
            return  # nothing to do
    
        last = arr[-1]                # save last element
        # shift elements right, scanning backwards to avoid overwrite
        for i in range(n - 1, 0, -1): # i = n-1, ..., 1
            arr[i] = arr[i - 1]
        arr[0] = last                 # place saved last at front
        # function mutates arr in place (no return needed for most judges)
